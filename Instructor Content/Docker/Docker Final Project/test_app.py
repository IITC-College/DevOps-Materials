#!/usr/bin/env python3
"""
Integration test suite for the Notes App Docker setup.
Tests both the Notebooks and Notes APIs via the Nginx reverse proxy (port 8080)
and directly against each service (ports 3000, 3001).
"""

import sys
import json
import time
import requests

BASE_URL = "http://localhost:8080"
NOTEBOOKS_DIRECT = "http://localhost:3000"
NOTES_DIRECT = "http://localhost:3001"

NOTEBOOKS_URL = f"{BASE_URL}/api/notebooks"
NOTES_URL = f"{BASE_URL}/api/notes"

# ── Colour helpers ────────────────────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

passed = 0
failed = 0


def ok(msg):
    global passed
    passed += 1
    print(f"  {GREEN}✓{RESET} {msg}")


def fail(msg, detail=""):
    global failed
    failed += 1
    print(f"  {RED}✗{RESET} {msg}")
    if detail:
        print(f"    {RED}{detail}{RESET}")


def section(title):
    print(f"\n{BOLD}{CYAN}{'─'*55}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'─'*55}{RESET}")


def assert_status(resp, expected, label):
    if resp.status_code == expected:
        ok(f"{label} → {resp.status_code}")
        return True
    else:
        fail(f"{label} → expected {expected}, got {resp.status_code}", resp.text[:200])
        return False


def assert_field(data, field, label):
    if field in data:
        ok(f"{label} has '{field}': {str(data[field])[:60]}")
        return True
    else:
        fail(f"{label} missing field '{field}'")
        return False


# ── Health checks ─────────────────────────────────────────────────────────────
section("Health Checks")

try:
    r = requests.get(f"{NOTEBOOKS_URL}/health", timeout=5)
    if assert_status(r, 200, "Notebooks health (via proxy)"):
        assert_field(r.json(), "message", "Response")
except requests.exceptions.ConnectionError:
    fail("Cannot connect to reverse proxy on port 8080 — is Docker running?")
    print(f"\n{YELLOW}Tip: run 'docker compose up' from the project root first.{RESET}\n")
    sys.exit(1)

try:
    r = requests.get(f"{NOTES_URL}/health", timeout=5)
    if assert_status(r, 200, "Notes health (via proxy)"):
        assert_field(r.json(), "message", "Response")
except requests.exceptions.ConnectionError:
    fail("Cannot connect to notes service via proxy")

# Direct service health checks
try:
    r = requests.get(f"{NOTEBOOKS_DIRECT}/api/notebooks/health", timeout=5)
    assert_status(r, 200, "Notebooks health (direct port 3000)")
except requests.exceptions.ConnectionError:
    fail("Cannot connect directly to notebooks service on port 3000")

try:
    r = requests.get(f"{NOTES_DIRECT}/api/notes/health", timeout=5)
    assert_status(r, 200, "Notes health (direct port 3001)")
except requests.exceptions.ConnectionError:
    fail("Cannot connect directly to notes service on port 3001")


# ── Notebooks CRUD ────────────────────────────────────────────────────────────
section("Notebooks — CRUD")

# Create
r = requests.post(NOTEBOOKS_URL, json={"name": "Test Notebook", "description": "Created by test_app.py"})
notebook_id = None
if assert_status(r, 201, "POST /api/notebooks"):
    data = r.json().get("data", {})
    assert_field(data, "_id", "Created notebook")
    assert_field(data, "name", "Created notebook")
    notebook_id = data.get("_id")

# Get all
r = requests.get(NOTEBOOKS_URL)
if assert_status(r, 200, "GET /api/notebooks"):
    notebooks = r.json().get("data", [])
    if isinstance(notebooks, list) and len(notebooks) >= 1:
        ok(f"Returned list with {len(notebooks)} notebook(s)")
    else:
        fail("Expected a non-empty list of notebooks")

# Get by ID
if notebook_id:
    r = requests.get(f"{NOTEBOOKS_URL}/{notebook_id}")
    if assert_status(r, 200, "GET /api/notebooks/:id"):
        assert_field(r.json().get("data", {}), "name", "Fetched notebook")

# Update
if notebook_id:
    r = requests.put(f"{NOTEBOOKS_URL}/{notebook_id}", json={"name": "Updated Notebook", "description": "Updated by test_app.py"})
    if assert_status(r, 200, "PUT /api/notebooks/:id"):
        data = r.json().get("data", {})
        if data.get("name") == "Updated Notebook":
            ok("Name was updated correctly")
        else:
            fail("Name was not updated", f"got: {data.get('name')}")

# 404 on unknown ID
r = requests.get(f"{NOTEBOOKS_URL}/000000000000000000000000")
assert_status(r, 404, "GET /api/notebooks/<bad-id> → 404")


# ── Notes CRUD ────────────────────────────────────────────────────────────────
section("Notes — CRUD (standalone, no notebookId)")

note_id = None

# Create standalone note
r = requests.post(NOTES_URL, json={"title": "Standalone Note", "content": "No notebook attached"})
if assert_status(r, 201, "POST /api/notes (standalone)"):
    data = r.json().get("data", {})
    assert_field(data, "_id", "Created note")
    assert_field(data, "title", "Created note")
    note_id = data.get("_id")

# Get all notes
r = requests.get(NOTES_URL)
if assert_status(r, 200, "GET /api/notes"):
    notes = r.json().get("data", [])
    if isinstance(notes, list) and len(notes) >= 1:
        ok(f"Returned list with {len(notes)} note(s)")
    else:
        fail("Expected a non-empty list of notes")

# Get by ID
if note_id:
    r = requests.get(f"{NOTES_URL}/{note_id}")
    if assert_status(r, 200, "GET /api/notes/:id"):
        assert_field(r.json().get("data", {}), "title", "Fetched note")

# Update
if note_id:
    r = requests.put(f"{NOTES_URL}/{note_id}", json={"title": "Updated Note", "content": "Updated by test_app.py"})
    if assert_status(r, 200, "PUT /api/notes/:id"):
        data = r.json().get("data", {})
        if data.get("title") == "Updated Note":
            ok("Title was updated correctly")
        else:
            fail("Title was not updated", f"got: {data.get('title')}")

# 404 on unknown ID
r = requests.get(f"{NOTES_URL}/000000000000000000000000")
assert_status(r, 404, "GET /api/notes/<bad-id> → 404")


# ── Cross-service: Note linked to a Notebook ─────────────────────────────────
section("Cross-service — Note linked to Notebook")

linked_note_id = None
if notebook_id:
    r = requests.post(NOTES_URL, json={
        "title": "Linked Note",
        "content": "This note belongs to a notebook",
        "notebookId": notebook_id
    })
    if assert_status(r, 201, f"POST /api/notes with notebookId"):
        data = r.json().get("data", {})
        stored_nb_id = str(data.get("notebookId", ""))
        if stored_nb_id == notebook_id:
            ok(f"notebookId stored correctly: {stored_nb_id}")
        else:
            fail("notebookId mismatch", f"expected {notebook_id}, got {stored_nb_id}")
        linked_note_id = data.get("_id")
else:
    print(f"  {YELLOW}⚠ Skipped (no notebook_id available){RESET}")


# ── Validation / Error Cases ──────────────────────────────────────────────────
section("Validation — Missing Required Fields")

r = requests.post(NOTEBOOKS_URL, json={"description": "No name"})
assert_status(r, 400, "POST /api/notebooks without 'name' → 400")

r = requests.post(NOTES_URL, json={"content": "No title"})
assert_status(r, 400, "POST /api/notes without 'title' → 400")

r = requests.post(NOTES_URL, json={"title": "No content"})
assert_status(r, 400, "POST /api/notes without 'content' → 400")


# ── Cleanup ───────────────────────────────────────────────────────────────────
section("Cleanup — Deleting test data")

if linked_note_id:
    r = requests.delete(f"{NOTES_URL}/{linked_note_id}")
    assert_status(r, 204, f"DELETE linked note")

if note_id:
    r = requests.delete(f"{NOTES_URL}/{note_id}")
    assert_status(r, 204, f"DELETE standalone note")

if notebook_id:
    r = requests.delete(f"{NOTEBOOKS_URL}/{notebook_id}")
    assert_status(r, 204, f"DELETE notebook")

    # Confirm gone
    r = requests.get(f"{NOTEBOOKS_URL}/{notebook_id}")
    assert_status(r, 404, "Deleted notebook returns 404")


# ── Summary ───────────────────────────────────────────────────────────────────
total = passed + failed
print(f"\n{BOLD}{'═'*55}{RESET}")
print(f"{BOLD}  Results: {GREEN}{passed} passed{RESET}{BOLD}, {RED}{failed} failed{RESET}{BOLD}, {total} total{RESET}")
print(f"{BOLD}{'═'*55}{RESET}\n")

sys.exit(0 if failed == 0 else 1)

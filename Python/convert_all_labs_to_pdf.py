#!/usr/bin/env python3
"""
Convert every Python lab's TASKS.md to a GitHub-styled PDF.
Uses the Python `markdown` library for MD→HTML and Chrome headless for HTML→PDF.
"""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Error: 'markdown' package not installed. Run: pip install markdown")

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]

GITHUB_CSS = """\
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
    color: #24292e;
    background-color: #ffffff;
}
h1 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; font-size: 2em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
h2 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; font-size: 1.5em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
h3 { font-size: 1.25em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
h4 { font-size: 1em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
p  { margin-top: 0; margin-bottom: 16px; }
ul, ol { padding-left: 2em; margin-top: 0; margin-bottom: 16px; }
li { margin-bottom: 0.25em; }
li + li { margin-top: 0.25em; }
code {
    background-color: rgba(175,184,193,0.2);
    padding: 0.2em 0.4em;
    font-size: 85%;
    border-radius: 3px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
pre {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
    margin-bottom: 16px;
}
pre code {
    background-color: transparent;
    padding: 0;
    white-space: pre;
}
hr {
    height: 0.25em;
    padding: 0;
    margin: 24px 0;
    background-color: #e1e4e8;
    border: 0;
}
blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
}
strong { font-weight: 600; }
table { border-spacing: 0; border-collapse: collapse; margin-bottom: 16px; }
table th, table td { padding: 6px 13px; border: 1px solid #dfe2e5; }
table tr { background-color: #fff; border-top: 1px solid #c6cbd1; }
table tr:nth-child(2n) { background-color: #f6f8fa; }
"""


def find_chrome() -> str | None:
    for path in CHROME_PATHS:
        if os.path.isfile(path):
            return path
    return None


def strip_language_labels(md_text: str) -> str:
    return re.sub(r"```[a-z]+\s*$", "```", md_text, flags=re.MULTILINE)


def md_to_html(md_text: str, title: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "sane_lists"],
    )
    return (
        f"<!DOCTYPE html>\n<html>\n<head>\n"
        f'<meta charset="UTF-8">\n<title>{title}</title>\n'
        f"<style>\n{GITHUB_CSS}</style>\n</head>\n<body>\n"
        f"{body}\n</body>\n</html>"
    )


def html_to_pdf(chrome: str, html_path: str, pdf_path: str) -> bool:
    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=30)
    return os.path.isfile(pdf_path)


def convert_lab(lab_dir: Path, chrome: str) -> bool:
    tasks_md = lab_dir / "TASKS.md"
    if not tasks_md.exists():
        return False

    folder_name = lab_dir.name
    title = folder_name.replace("_", " ").title()
    pdf_name = f"{folder_name}_TASKS.pdf"
    pdf_path = lab_dir / pdf_name

    md_text = tasks_md.read_text(encoding="utf-8")
    md_text = strip_language_labels(md_text)
    html_content = md_to_html(md_text, title)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(html_content)
        tmp_html = tmp.name

    try:
        success = html_to_pdf(chrome, tmp_html, str(pdf_path))
    finally:
        os.unlink(tmp_html)

    return success


def main():
    print("=========================================")
    print("  Python Labs -> PDF Batch Converter")
    print("=========================================\n")

    chrome = find_chrome()
    if not chrome:
        sys.exit("Error: Google Chrome not found. Install Chrome to generate PDFs.")

    print(f"Using Chrome: {chrome}\n")

    labs_root = Path(__file__).resolve().parent
    lab_dirs = sorted(
        [d for d in labs_root.iterdir() if d.is_dir() and (d / "TASKS.md").exists()]
    )

    if not lab_dirs:
        sys.exit("No lab folders with TASKS.md found.")

    print(f"Found {len(lab_dirs)} labs to convert.\n")

    success_count = 0
    fail_count = 0

    for lab_dir in lab_dirs:
        lab_name = lab_dir.name
        print(f"  Converting {lab_name} ... ", end="", flush=True)
        if convert_lab(lab_dir, chrome):
            print("OK")
            success_count += 1
        else:
            print("FAILED")
            fail_count += 1

    print(f"\n=========================================")
    print(f"  Done!  {success_count} converted, {fail_count} failed")
    print(f"=========================================\n")


if __name__ == "__main__":
    main()

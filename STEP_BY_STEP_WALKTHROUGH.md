# Lab 10 – Step-by-Step Solver Walkthrough

This document traces the lab as a student would solve it, step by step. **Current directory is tracked in [brackets].**

---

## Start

- **Location:** Lab root `linux_lab10_default_permissions/`
- **Action:** From README: run `cd clues/level1 && cat clue1.txt`

---

## Level 1

### After entry command
- **[clues/level1]** – I ran `cd clues/level1 && cat clue1.txt`, so I'm in `clues/level1/`.

### Clue 1 (Check umask)
- **Instructions:** Run `umask`, then `umask -S`. Write down value.
- **NEXT STEP:** `cat clue2.txt`
- **Action:** I run `cat clue2.txt` (still in clues/level1).
- **[clues/level1]**

### Clue 2 (Create file, observe permissions)
- **Instructions:** `touch test_file.txt`, `ls -l test_file.txt`, calculate 666 − umask, verify.
- **Effect:** I create `test_file.txt` in current dir → **clues/level1/test_file.txt**.
- **NEXT STEP:** `cat clue3.txt`
- **Action:** `cat clue3.txt`
- **[clues/level1]**

### Clue 3 (Create directory, observe permissions)
- **Instructions:** `mkdir test_directory`, `ls -ld test_directory`, calculate 777 − umask.
- **Effect:** I create **clues/level1/test_directory/**.
- **NEXT STEP:** `cd ../level2` then `cat clue1.txt`
- **Action:** `cd ../level2` → **[clues/level2]** → `cat clue1.txt`

---

## Level 2

### Clue 1 (Analyze files with different umasks)
- **Instructions:**
  1. `cd ../../data/examples` → from clues/level2, that goes to **data/examples/**.
  2. `ls -la`, then `ls -l umask_022/`, `umask_027/`, `umask_077/`, then `ls -ld` for each.
  3. HINT: `cat ../logs/permissions_history.log` (from data/examples, `../logs` = data/logs) ✓
- **NEXT STEP:** `cd ../../clues/level2` then `cat clue2.txt`
- **Action:** I'm in **data/examples**. I run `cd ../../clues/level2` → **[clues/level2]** → `cat clue2.txt`

### Clue 2 (Calculate expected permissions)
- **Where I am:** [clues/level2]
- **Instructions:** Calculate 666−umask and 777−umask for 022, 027, 077, 002. Then verify using files in data/examples/. Clue says: if in clues/level2, run `cd ../../data/examples` first.
- **If I go to verify:** I run `cd ../../data/examples` → **[data/examples]**, run ls there, then use NEXT STEP from here.
- **NEXT STEP:** `cd ../../clues/level2` then `cat clue3.txt`
  - From **[data/examples]:** `cd ../../clues/level2` → lab root then clues/level2 → **[clues/level2]** ✓
  - From **[clues/level2]:** same command leaves me in **[clues/level2]** ✓
- **Action:** `cd ../../clues/level2` → `cat clue3.txt`
- **[clues/level2]**

### Clue 3 (Security implications)
- **Instructions:**
  1. `cd ../../projects` → from clues/level2 → **[projects]**
  2. Explore secure_files/, shared_team/, default_app/, cat READMEs, ls -l each.
- **NEXT STEP:** `cd ../../clues/level3` then `cat clue1.txt`
- **Action:** I'm in **projects**. I run `cd ../../clues/level3` → **[clues/level3]** → `cat clue1.txt` ✓

---

## Level 3

### Clue 1 (Change umask temporarily)
- **[clues/level3]**
- **Instructions:** Note umask, `umask 027`, `touch test_umask_027.txt`, `ls -l`, `mkdir test_umask_027_dir`, `ls -ld`. Then try umask 077 and 022, create more test files.
- **Effect:** Files/dirs created in current dir → **clues/level3/** (e.g. test_umask_027.txt, test_umask_077.txt, test_umask_022.txt, test_umask_027_dir). Slightly messy but valid.
- **NEXT STEP:** `cat clue2.txt`
- **Action:** `cat clue2.txt`
- **[clues/level3]**

### Clue 2 (Real-world scenarios)
- **Instructions:** umask 077 → touch private_secret.txt; umask 027 → touch team_project.txt; umask 022 → touch web_content.txt. HINT: `cat ../../data/logs/permissions_history.log` (from clues/level3, ../../data = lab_root/data) ✓
- **NEXT STEP:** `cat clue3.txt`
- **Action:** `cat clue3.txt`
- **[clues/level3]**

### Clue 3 (Synthesis challenge)
- **Instructions:** Determine 640, umask 026, `umask 026`, `touch final_test.txt`, verify. HINT: `cat ../../data/secrets/tips.txt` ✓
- **FINAL STEP:** `cd ../..` then `touch my_answers.txt`
- **Action:** From **[clues/level3]**, `cd ../..` → **[lab root]** ✓ Then `touch my_answers.txt` → **lab_root/my_answers.txt** ✓

---

## Summary

| Step        | My directory    | Command / action                    | Result / next location   |
|------------|-----------------|-------------------------------------|--------------------------|
| Entry      | lab root        | cd clues/level1 && cat clue1.txt   | clues/level1             |
| L1 clue1→2 | clues/level1    | cat clue2.txt                       | clues/level1             |
| L1 clue2→3 | clues/level1    | cat clue3.txt                      | clues/level1             |
| L1→L2      | clues/level1    | cd ../level2 && cat clue1.txt      | clues/level2             |
| L2 c1      | clues/level2    | cd ../../data/examples             | data/examples            |
| L2 c1→c2   | data/examples   | cd ../../clues/level2 && cat clue2 | clues/level2             |
| L2 c2→c3   | clues/level2    | cd ../../clues/level2 && cat clue3 | clues/level2             |
| L2 c3      | clues/level2    | cd ../../projects                  | projects                 |
| L2→L3      | projects        | cd ../../clues/level3 && cat clue1 | clues/level3             |
| L3 c1→c2   | clues/level3    | cat clue2.txt                      | clues/level3             |
| L3 c2→c3   | clues/level3    | cat clue3.txt                      | clues/level3             |
| Final      | clues/level3    | cd ../.. && touch my_answers.txt   | lab root, file created   |

**Verdict:** The flow is consistent. Every path works from the directory the student is in after the previous step. NEXT STEPs and FINAL STEP lead to the correct directories and files. One clarification was added in Level 2 clue2: how to get to data/examples when starting from clues/level2 for verification.

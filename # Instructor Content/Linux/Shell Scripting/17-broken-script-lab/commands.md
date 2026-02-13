# Commands

```bash
# Try broken scripts first (they will fail or behave wrong)
bash deploy_broken.sh
bash check_broken.sh
bash backup_broken.sh
bash confirm_broken.sh

# Demo confirm_broken: press Enter (empty) - script may error
# Demo confirm_fixed: empty = "Cancelled", yes = "Restarting"

# Compare with fixed versions
chmod +x deploy_fixed.sh check_fixed.sh backup_fixed.sh confirm_fixed.sh
./deploy_fixed.sh
./check_fixed.sh
./backup_fixed.sh
./confirm_fixed.sh
```

Find the bugs in _broken scripts, then compare with _fixed.

# Commands

```bash
chmod +x deploy.sh check.sh backup.sh check_log_exists.sh validate_before_deploy.sh check_readable.sh
./deploy.sh
./check.sh
./backup.sh
./check_log_exists.sh
./validate_before_deploy.sh prod
./validate_before_deploy.sh
./check_readable.sh
```

Demo: create config.txt for deploy/check_readable; create logs/ and logs/app.log for check/check_log_exists; try empty path and a dir for backup; run validate with and without argument.

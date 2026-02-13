# Commands

```bash
# Why ./script fails? Check permissions
ls -l deploy.sh check.sh backup.sh debug_example.sh

chmod +x deploy.sh check.sh backup.sh debug_example.sh
./deploy.sh
./check.sh
./backup.sh
./debug_example.sh
./debug_example.sh /wrong/path
```

Demo: uncomment DEBUG echo lines in scripts. Run debug_example.sh with no arg (config.txt) and with a path - see pwd and ls -l output.

# Commands

```bash
chmod +x deploy.sh check.sh flow_demo.sh
./deploy.sh
echo $?
./check.sh app
./flow_demo.sh
echo $?
touch config.txt
./flow_demo.sh
echo $?
```

Demo: deploy without config (DEBUG + exit 1); flow_demo fails at step 1, then passes with config.

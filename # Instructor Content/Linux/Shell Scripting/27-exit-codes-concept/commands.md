# Commands

```bash
chmod +x deploy.sh check.sh demo_exit.sh run_deploy_with_check.sh
./deploy.sh
echo $?
echo 'APP_NAME=myapp' > config.txt
./deploy.sh config.txt
echo $?
./check.sh
echo $?
mkdir logs
./demo_exit.sh
echo $?
./run_deploy_with_check.sh config.txt
```

Demo: deploy without config (exit 1); with config (exit 0). check without logs (1), with logs (0). run_deploy_with_check runs check then deploy; fails if check fails.

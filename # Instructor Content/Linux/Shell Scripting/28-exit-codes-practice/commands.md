# Commands

```bash
# Simple exit code demos
chmod +x deploy.sh check.sh chain.sh
echo 'APP_NAME=myapp' > config.txt
./deploy.sh
echo $?
./check.sh
# type nginx or postgres or app
echo $?
./chain.sh
# type nginx when check prompts

# CI/CD Pipeline (scripts depend on each other via exit codes)
chmod +x ci_validate.sh ci_build.sh ci_test.sh ci_deploy.sh pipeline.sh
echo 'APP_NAME=myapp' > config.txt
./pipeline.sh config.txt staging

# Run steps individually to see dependencies:
./ci_validate.sh config.txt
./ci_build.sh config.txt
./ci_test.sh config.txt
./ci_deploy.sh config.txt staging

# Fail validate: remove config.txt, run pipeline again - stops at validate
# Fail build: remove .validated, run ci_build - fails
```

Demo: pipeline runs validate -> build -> test -> deploy; any step exit 1 aborts the rest.

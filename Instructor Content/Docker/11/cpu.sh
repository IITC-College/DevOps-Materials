## Hard limit -> The container will not be able to use more than 0.5 CPU
# CPU 0.5
docker run -d --rm \
  --name cpu-decimals \
  --cpus="0.5" \
  busybox sh -c "while true; do :; done"

# CPU 1.5
docker run -d --rm \
  --name cpu-decimals \
  --cpus="1.5" \
  busybox sh -c "while true; do :; done"

## Relative limit -> The container will be able to use up to 1.5 CPU
docker run -d --rm \
  --name cpu-shares_low \
  --cpuset-cpus="0" \
  --cpu-shares=512 \
  busybox sh -c "while true; do :; done"
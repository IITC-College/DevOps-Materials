docker run -d \
  --name no_restart \
  busybox sh -c "sleep 3 && exit 1"
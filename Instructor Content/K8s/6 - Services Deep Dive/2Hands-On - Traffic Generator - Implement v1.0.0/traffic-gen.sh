#!/bin/sh

# ./traffic-gen.sh www.google.com 1

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <target> <interval>"
  exit 1
fi

TARGET=$1
INTERVAL=$2

echo "Sending traffic to $TARGET every $INTERVAL seconds..."

while true; do
  REQUEST_TIME=$(date +"%Y-%m-%d %H:%M:%S")
  RESPONSE=$(curl -s "$TARGET")

  echo "[$REQUEST_TIME] $RESPONSE"
  
  sleep $INTERVAL
done
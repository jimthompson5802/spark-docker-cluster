#!/bin/bash

/usr/local/spark/sbin/start-slave.sh spark://master:7077  $@

# keep this script alive so container stays active
while [ 1 -eq 1 ]
do
  sleep 60
done


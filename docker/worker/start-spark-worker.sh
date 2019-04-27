#!/bin/bash

/usr/local/spark/sbin/start-slave.sh  $@

# keep this script alive so container stays active
while [ 1 -eq 1 ]
do
  sleep 60
done


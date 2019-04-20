#!/bin/bash

/usr/local/spark/sbin/start-worker.sh $@
while [ 1 -eq 1 ]
do
  sleep 60
done


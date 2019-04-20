#!/bin/bash

# Arguements
#  $1: Directory to be mounted to the PySpark Jupyter NB container (pyspnb)
#  $2: Directory for persistent store that is mounted to all containers at /spark/data.
#      This simulates a distributed file system.

CODE_DIR=$1  DATA_DIR=$2 docker-compose up --detach
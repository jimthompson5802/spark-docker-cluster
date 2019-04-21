#!/bin/bash

# Arguements
#  $1: Directory to be mounted to the PySpark Jupyter NB container (pyspnb)
#  $2: Directory for persistent store that is mounted to all containers at /spark/data.
#      This simulates a distributed file system.

code_dir=${1:-$PWD/project}
data_dir=${2:-$PWD/data}

echo $code_dir  $data_dir

CODE_DIR=$code_dir  DATA_DIR=$data_dir docker-compose up --detach
#!/bin/bash

APACHE_SPARK_VERSION=2.3.3
HADOOP_VERSION=2.7
PY4J_VERSION=0.10.7


docker build --build-arg APACHE_SPARK_VERSION=$APACHE_SPARK_VERSION \
    --build-arg HADOOP_VERSION=$HADOOP_VERSION \
    --build-arg PY4J_VERSION=$PY4J_VERSION \
    -t spark-base:$APACHE_SPARK_VERSION base

docker build \
    -t spark-master:$APACHE_SPARK_VERSION master

docker build \
    -t spark-worker:$APACHE_SPARK_VERSION worker

docker build \
    -t spark-pyspnb:$APACHE_SPARK_VERSION pyspnb
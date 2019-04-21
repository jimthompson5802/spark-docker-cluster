#!/bin/bash

ANACONDA3_VERSION=5.3.0
APACHE_SPARK_VERSION=2.4.1
HADOOP_VERSION=2.7
PY4J_VERSION=0.10.7

docker build --build-arg APACHE_SPARK_VERSION=$APACHE_SPARK_VERSION \
    --build-arg HADOOP_VERSION=$HADOOP_VERSION \
    --build-arg PY4J_VERSION=$PY4J_VERSION \
    --build-arg ANACONDA3_VERSION=$ANACONDA3_VERSION \
    -t spark-base:$APACHE_SPARK_VERSION base

docker build \
    --build-arg APACHE_SPARK_VERSION=$APACHE_SPARK_VERSION \
    -t spark-master:$APACHE_SPARK_VERSION master

docker build \
    --build-arg APACHE_SPARK_VERSION=$APACHE_SPARK_VERSION \
    -t spark-worker:$APACHE_SPARK_VERSION worker

docker build \
    --build-arg APACHE_SPARK_VERSION=$APACHE_SPARK_VERSION \
    -t spark-pyspnb:$APACHE_SPARK_VERSION pyspnb
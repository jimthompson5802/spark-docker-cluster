#!/bin/bash


# Parameters:
#  $1 - image tag to remove

image_tag=${1:-2.3.3}

docker rmi spark-base:$image_tag || true
docker rmi spark-master:$image_tag || true
docker rmi spark-worker:$image_tag || true
docker rmi spark-pyspnb:$image_tag || true

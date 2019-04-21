# Stand-alone Spark Cluster Using Docker Containers

## Overview

![Architecture Overview](./images/architecture_slide.jpg)


## Building the Docker Images
Three Docker images are required to run the Spark cluster:
* `spark-master` - Spark Stand-alone Cluster manager
* `spark-worker` - Spark worker process
* `spark-pyspnb` - PySpark Jupyter Notebook Server

These three images are based on a custom `spark-base` image built using the [`continuumio/anaconda3`](https://hub.docker.com/r/continuumio/anaconda3/), which provides the the required Python libraries.  To this image we add the following to provide the Spark run-time:
* Java 1.8
* Apache Spark ([pre-built binaries](https://spark.apache.org/downloads.html))
* Miscellenous system utilities to support running Apache Spark

Run the following command to build the required images:
```
cd docker
./build_images.sh
```

## Starting Stand-alone Spark Cluster
From the root directory execute this command
```
bin/start_spark_cluster $PWD/project $PWD/data
```


## Shutdown Stand-alone Spark Cluster
From the root directory execute this command
```
docker-compose down
```
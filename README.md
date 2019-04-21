# Stand-alone Spark Cluster Using Docker Containers

## Overview

![Architecture Overview](./images/architecture_slide.jpg)


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
#!/bin/bash



PYSPARK_DRIVER_PYTHON="jupyter" \
PYSPARK_DRIVER_PYTHON_OPTS="notebook --NotebookApp.token='' --notebook-dir=/opt/project \
    --allow-root --ip='*'  --port=8888 --no-browser" \
pyspark --master spark://spark-master:7077
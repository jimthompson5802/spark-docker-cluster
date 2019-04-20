FROM spark-base:2.3.3


ENV PYSPARK_DRIVER_PYTHON "jupyter"
ENV PYSPARK_DRIVER_PYTHON_OPTS "notebook --NotebookApp.token='' --notebook-dir=/opt/project \
    --allow-root --ip='*'  --port=8888 --no-browser"
ENV SPARK_PUBLIC_DNS "localhost"

COPY start-pyspnb.sh /spark
RUN chmod 755 /spark/start-pyspnb.sh


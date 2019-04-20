FROM spark-base:2.3.3

COPY pyspark_jupyter_notebook.sh /sbin
RUN chmod 755 /sbin/pyspark_jupyter_notebook.sh

ENV PYSPARK_DRIVER_PYTHON "jupyter"

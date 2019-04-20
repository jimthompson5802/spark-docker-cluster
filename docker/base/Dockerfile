FROM continuumio/anaconda3:5.3.0

# Version Specification
ARG APACHE_SPARK_VERSION
ARG HADOOP_VERSION
ARG PY4J_VERSION

# install pre-reqs
RUN apt-get update -y && apt-get -y install openjdk-8-jdk net-tools procps

# install Spark
RUN curl -s http://mirror.reverse.net/pub/apache/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# set up environment variables
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-${PY4J_VERSION}-src.zip
ENV PATH /opt/conda/bin:$SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON=/opt/conda/bin/python





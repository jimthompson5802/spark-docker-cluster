ARG APACHE_SPARK_VERSION
FROM spark-base:${APACHE_SPARK_VERSION}

ENV SPARK_PUBLIC_DNS "localhost"

COPY start-pyspnb.sh /spark
RUN chmod 755 /spark/start-pyspnb.sh


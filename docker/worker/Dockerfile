FROM spark-base:2.3.3

ENV SPARK_PUBLIC_DNS "localhost"

COPY start-spark-worker.sh /spark
RUN chmod 755 /spark/start-spark-worker.sh

from pyspark.sql import SparkSession, Row
import socket
import os


# function to create data frame
def create_data(x):
    hostname = socket.gethostname()
    pid = os.getpid()
    return Row(x=x, times2x=2*x, hostname=hostname, pid=pid)


if __name__ == "__main__":

    spark = SparkSession.builder \
        .appName('PySpark - Test') \
        .enableHiveSupport() \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel('WARN')


    rdd1 = sc.parallelize(range(2000))
    df = spark.createDataFrame(rdd1.map(lambda x: create_data(x))).cache()

    df.createOrReplaceTempView('my_table')

    spark.sql("select * from my_table limit 5").show()


    spark.sql("""
select hostname, pid, count(*) as element_count 
from my_table 
group by hostname, pid
order by hostname, pid
    """).show()

    spark.stop()

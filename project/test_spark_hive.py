import pytest
import numpy as np
import os
from collections import namedtuple
from pyspark.sql import SparkSession, Row


SparkRunTime = namedtuple("SparkRunTime",['spark', 'sc', 'storage_platform'])

# config
NUMBER_OF_ROWS = 1000
NUMBER_OF_COLS = 8
NUMBER_BLOCKS = 2
NUMBER_PARTITIONS = NUMBER_BLOCKS

storage_platform = "file:///spark/data"


hive_table_ddl = """
CREATE EXTERNAL TABLE hive_table(
   X_1 double,
   X_2 double,
   X_3 double,
   X_4 double,
   X_5 double,
   X_6 double,
   X_7 double,
   X_8 double,
   part_id1 string,
   part_id2 string
)
STORED AS parquet"""


def test_hive_operation():

    spark = SparkSession.builder \
        .appName('EMR/Spark Test') \
        .config('spark.driver.memory', '2G') \
        .config("spark.driver.maxResultSize", "2g") \
        .config('spark.executor.memory', '4g') \
        .config('spark.master', 'spark://master:7077') \
        .enableHiveSupport() \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel('WARN')


    #
    # HIVE oriented operations
    #
    def combineData(x):
        x[0].update(x[1])
        return x[0]

    def generate_some_data(seed):
        np.random.seed(seed)

        colnames = ['X_' + str(i + 1) for i in range(NUMBER_OF_COLS)]
        numerics = np.round(np.random.randn(NUMBER_OF_ROWS, NUMBER_OF_COLS), 3)
        numeric_list = numerics.tolist()
        numeric_data = [dict(zip(colnames, a_row)) for a_row in numeric_list]

        chr_list = zip([str(x) for x in np.random.choice(list('abcde'), NUMBER_OF_ROWS)],
                       [str(x) for x in np.random.choice(list('xyz'), NUMBER_OF_ROWS)])
        chrnames = ['part_id1', 'part_id2']
        chr_data = [dict(zip(chrnames, a_row)) for a_row in chr_list]

        return [Row(**kw) for kw in map(combineData, zip(numeric_data, chr_data))]

    my_rdd = sc.parallelize(range(NUMBER_BLOCKS), NUMBER_PARTITIONS).flatMap(generate_some_data)
    my_df = spark.createDataFrame(my_rdd)

    my_df.write.parquet(os.path.join(storage_platform, 'my_data_parquet'),
                        mode='overwrite')

    # clean old table
    spark.sql("DROP TABLE IF EXISTS hive_table PURGE")

    hive_sql_cmd = hive_table_ddl + " LOCATION '" + os.path.join(storage_platform,"my_data_parquet") + "'"

    spark.sql(hive_sql_cmd)

    answer_df = spark.sql("select * from hive_table limit 5")
    answer_df.show()
    assert answer_df.first().X_1 == 1.624
    assert answer_df.first().X_8 == -0.761

    number_rows = spark.sql("select count(*) as row_count from hive_table").first().row_count
    assert number_rows == NUMBER_BLOCKS * NUMBER_OF_ROWS

    spark.sql("DROP TABLE IF EXISTS hive_table PURGE")



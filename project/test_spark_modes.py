import pytest
from pyspark.sql import SparkSession



@pytest.mark.parametrize("master, deploy_mode", [
    ('local[*]', None),
    ('local[2]', None),
])
def test_simple_operation(master, deploy_mode):

    spark_config = SparkSession.builder \
        .appName('EMR/Spark Test') \
        .config('spark.driver.memory', '2G') \
        .config("spark.driver.maxResultSize", "2g") \
        .config('spark.executor.memory', '4g')

    if master == 'yarn':
        spark = spark_config \
            .config('spark.master', master) \
            .config('spark.submit.deployMode', deploy_mode) \
            .enableHiveSupport() \
            .getOrCreate()
    else:
        spark = spark_config \
            .config('spark.master', master) \
            .enableHiveSupport() \
            .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel('WARN')


    rdd1 = sc.parallelize(range(10))
    my_list = rdd1.map(lambda x: (x, 2*x)).collect()

    assert my_list[0][0] == 0
    assert my_list[9][1] == 18

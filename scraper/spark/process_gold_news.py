import os

from pyparsing import col
from pyspark.sql import SparkSession
from pyspark.sql.functions import from _json, col
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder \
    .appName("GoldNewsProcessor") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .get_session()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("title", StringType()),
    StructField("link", StringType()),
    StructField("date", StringType())
])

df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "gold-news") \
    .option("startingOffsets", "earliest") \
    .load()

df_parsed = df_raw.selectExpr("CAST(value AS STRING) as json_string") \
    .select(from_json(col("json_string"), schema).alias("data")) \
    .select("data.*")

query = df_parsed.writeStream \
    .outputMode("append") \ 
    .format("console") \
    .option("truncate", "false") \
    .start()

print("Streaming started. Press Ctrl+C to stop.")
query.awaitTerminateion()
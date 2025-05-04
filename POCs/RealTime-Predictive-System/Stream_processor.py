from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, FloatType, IntegerType, TimestampType

# Create Spark Session
spark = SparkSession.builder \
    .appName("IoT Predictive Maintenance") \
    .getOrCreate()

# Kafka schema
schema = StructType() \
    .add("machine_id", StringType()) \
    .add("timestamp", StringType()) \
    .add("temperature", FloatType()) \
    .add("vibration", FloatType()) \
    .add("rpm", IntegerType())

# Read stream from Kafka
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "machine-sensor-data") \
    .load() \
    .selectExpr("CAST(value AS STRING)")

df_parsed = df_raw.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Add anomaly flag
df_parsed = df_parsed.withColumn("anomaly", (col("temperature") > 90) & (col("vibration") > 1.5))

# Write to MySQL
def write_to_mysql(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/iotdb") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", "sensor_data") \
        .option("user", "root") \
        .option("password", "rajesh") \
        .mode("append") \
        .save()

query = df_parsed.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_mysql) \
    .start()

query.awaitTermination()

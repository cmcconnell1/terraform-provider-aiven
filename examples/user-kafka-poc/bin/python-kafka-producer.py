#!/usr/bin/env python3

from kafka import KafkaProducer

brokers = ['samplekafka-senior-b7bb.aivencloud.com:26096']

    #bootstrap_servers="samplekafka-senior-b7bb.aivencloud.com:26096",
    #bootstrap_servers="https://avnadmin:hnlh4jllvd9658h5@samplekafka-senior-b7bb.aivencloud.com:26088"

producer = KafkaProducer(
    bootstrap_servers=brokers, 
    #api_version=(0, 11, 5),
    #api_version=(0, 10, 1),
    # trying some hardcoded versions per https://github.com/dpkp/kafka-python/blob/master/kafka/producer/kafka.py#L393
    #api_version=(0, 8, 2),
    #api_version=(2, 1, 0),
    # https://readthedocs.org/projects/kafka-python/downloads/pdf/master/
    api_version_auto_timeout_ms=3000,
    security_protocol="SSL",
    ssl_cafile="~/work/aiven/kafkaCerts/ca.pem",
    ssl_certfile="~/work/aiven/kafkaCerts/service.cert",
    ssl_keyfile="~/work/aiven/kafkaCerts/service.key",
)

for i in range(1, 4):
    message = "message number {}".format(i)
    print("Sending: {}".format(message))
    producer.send("demo-topic", message.encode("utf-8"))

# Force sending of all messages

producer.flush()

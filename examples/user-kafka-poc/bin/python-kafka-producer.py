#!/usr/bin/env python3

from kafka import KafkaProducer

brokers = ['samplekafka-senior-b7bb.aivencloud.com:26086']
#brokers = ['34.78.237.191:26096']


    #bootstrap_servers="samplekafka-senior-b7bb.aivencloud.com:26096",
    #bootstrap_servers="https://avnadmin:hnlh4jllvd9658h5@samplekafka-senior-b7bb.aivencloud.com:26088"

producer = KafkaProducer(
    bootstrap_servers=brokers, 
    #api_version=(0, 11, 5),
    # ref: https://python.developreference.com/article/10948208/Cannot+connect+to+Kafka+from+Flask+in+a+dockerized+environement
    #api_version=(0, 10, 1),
    # trying some hardcoded versions per https://github.com/dpkp/kafka-python/blob/master/kafka/producer/kafka.py#L393
    #api_version=(0, 8, 2),
    #api_version=(2, 1, 0),
    # https: // github.com/dpkp/kafka-python/issues/1308
    # https://github.com/dpkp/kafka-python/issues/1308#issuecomment-469227827
    #request_timeout_ms=3000,
    # https://readthedocs.org/projects/kafka-python/downloads/pdf/master/
    api_version_auto_timeout_ms=3000,
    security_protocol="SSL",
    ssl_cafile="/Users/cmcc/work/aiven/kafkaCerts/service.key",
    ssl_certfile="/Users/cmcc/work/aiven/kafkaCerts/service.cert",
    ssl_keyfile="/Users/cmcc/work/aiven/kafkaCerts/ca.pem"
)

for i in range(1, 4):
    message = "message number {}".format(i)
    print("Sending: {}".format(message))
    producer.send("demo-topic", message.encode("utf-8"))

# Force sending of all messages

producer.flush()

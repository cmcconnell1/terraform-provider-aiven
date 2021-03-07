
# Kafka

#### Connect to docker instance
```
docker run -it --rm mesosphere/kafka-client
```

#### Create topic with default settings
```
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --create --topic demo_topic --partitions 1 --replication-factor 3 
```

#### Create topic with custom cleanup policy
```
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --create --topic _schemas --partitions 1 --replication-factor 3  --config cleanup.policy=compact
```

#### List topics
```
/bin/kafka-topics.sh --zookeeper  zk.demo.com:2181/kafka --list
```

#### Describe topics
```
/bin/kafka-topics.sh --describe --zookeeper zk.demo.com:2181/kafka --topic demo_topic
```

####  Change retention
```
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --alter --topic demo_topic --config retention.ms=14400000
```

#### Alter topic
```
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --alter --topic demo_topic 
kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --alter --config cleanup.policy=compact --topic _schemas
```

#### Produce message
```
echo "Hello, World" | /bin/kafka-console-producer.sh --broker-list kafka.demo.com:9092 --topic demo_topic
```

#### Consume messages
```
/bin/kafka-console-consumer.sh --zookeeper zk.amazonaws.com:2181/nonprod-kafka --topic demo_topic --from-beginning
```

#### Delete topics
```
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --delete --topic _schemas
```

From <https://github.com/confluentinc/schema-registry/issues/698> 

#### Graceful shutdown
```
/bin/kafka-server-stop.sh
```

#### List the consumer groups known to Kafka
```
/bin/kafka-consumer-groups.sh --new-consumer --bootstrap-server kafka.demo.com:9092 --list
```

#### View the details of a consumer group
```
/bin/kafka-consumer-groups.sh --zookeeper zk.demo.com:2181/kafka --describe --group <group name>
```

```
for i in `/bin/kafka-consumer-groups.sh --new-consumer --bootstrap-server kafka.demo.com:9092 --list`; do /bin/kafka-consumer-groups.sh --zookeeper zk.demo.com:2181/kafka --describe --group $i; done
```

#### Janitor
```
docker run mesosphere/janitor /janitor.py -r cassandra_role -p cassandra_principal -z master.mesos:2181

• -r: The role of the resources to be deleted
• -p: The principal of the resources to be deleted
• -z: The configuration zookeeper node to be deleted
```

for i in {1..10}; do echo "Hello, World.."$i | /bin/kafka-console-producer.sh --request-required-acks -1 --broker-list kafka1.demo.com:9092,kafka2.demo.com:9092,kafka3.demo.com:9092 --topic demo_topic ; done

#### 
```
./bin/kafka-run-class.sh kafka.tools.ConsumerOffsetChecker --broker-info --group test_group --topic test_topic --zookeeper localhost:2181
Group           Topic                  Pid Offset          logSize         Lag             Owner
test_group      test_topic             0   698020          698021          1              test_group-0
test_group      test_topic             1   235699          235699          0               test_group-1
test_group      test_topic             2   117189          117189          0               test_group-2
```

#### Produce AVRO messages

#### Consume AVRO messages

#### Kafka broker list
```
dcos kafka--name=confluent-kafka connection
dcos kafka --name=confluent-kafka

https://github.com/Landoop/kafka-topics-ui
```
#### List consumer group

#### From Zookeeper shell list path where Kafka stores consumers' offsets like this:
```
./bin/zookeeper-shell.sh localhost:2181
ls /consumers
```
```
/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list kafka.demo.com:9092 --topic demo_topic --time -1 | while IFS=: read topic_name partition_id number; do echo "$number"; done | paste -sd+ - | bc 9
```
```
/bin/kafka-consumer-groups.sh --list --zookeeper zk.demo.com:2181
```
#### Check the number of messages read and written, as well as the lag for each consumer in a specific consumer group. For example:
```
$ /bin/kafka-consumer-offset-checker.sh --group flume --topic t1 --zookeeper zk.demo.com:2181
```

```
/bin/kafka-consumer-offset-checker.sh --group console-consumer-74649 --topic demo_topic --zookeeper zk.demo.com:2181
```

#### List all groups
```
sh /tmp/kafka_2.11-0.10.2.0/bin/kafka-consumer-groups.sh --list --zookeeper zk.demo.com:2181 > in.txt
echo 'console-consumer-74649' > in.txt
```
#### Find topic in group
```
for i in `cat in.txt`; do /tmp/kafka_2.11-0.10.2.0/bin/kafka-consumer-offset-checker.sh --group console-consumer-74649 --topic demo_topic --zookeeper zk.demo.com:2181;done > /in1.txt
cat in1.txt |grep demo_topic|grep -v "Exiting due to: org.apache.zookeeper" |awk '{print$(NF-1)}'|grep -vi unknown > in2.txt
python -c 'print(sum(int(l) for l in open("in2.txt")))'
```

#### List all groups
```
> sh /tmp/kafka_2.11-0.10.2.0/bin/kafka-consumer-groups.sh --list --zookeeper zk.demo.com:2181 > in.txt
```

#### Find topic in group
```
> for i in `cat in.txt`; do sh /tmp/kafka_2.11-0.10.2.0/bin/kafka-consumer-offset-checker.sh --group $i --topic demo_topic --zookeeper zk.demo.com:2181;done 2> /dev/null > /in1.txt
> cat in1.txt |grep demo_topic|grep -v "Exiting due to: org.apache.zookeeper" |awk '{print$(NF-1)}'|grep -vi unknown > in2.txt
> python -c 'print(sum(int(l) for l in open("in2.txt")))'
> EOF
```

#### Kafka version
```
find ./libs/ -name \*kafka_\* | head -1 | grep -o '\kafka[^\n]*'
kafka_2.11-0.10.1.0.jar.asc
```

#### To check lag in kafka
```
./kafka-run-class.sh kafka.admin.ConsumerGroupCommand --describe --group console-consumer-74649 --zookeeper zk.demo.com:2181
```

```
./kafka-run-class.sh kafka.admin.ConsumerGroupCommand --describe --group console-consumer-74649 --bootstrap-server kafka.demo.com:9092 
```

#### Highest available Kafka Topic/Partition Offset
```
./bin/kafka-run-class kafka.tools.GetOffsetShell --broker-list <host>:<port> --topic <topic-name> --partition <partition-number> --time -1
```
#### Lowest available Kafka Topic/Partition Offset:
```
sh /bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list kafka.demo.com:9092 --topic demo_topic --time -2
```
```
/bin/kafka-consumer-groups.sh --list --zookeeper zk.demo.com:2181
console-consumer-51753
```
```
for i in `/bin//kafka-consumer-groups.sh --list --zookeeper zk.demo.com:2181/kafka`;do /bin/kafka-consumer-groups.sh --zookeeper zk.demo.com:2181/kafka --group $i --describe;done
```

####  To rebalance load
```
/bin/kafka-preferred-replica-election.sh --zookeeper zk01.demo.com:2181,zk02.demo.com:2181,zk03.demo.com:2181/kafka
Successfully started preferred replica election for partitions Set([loadtest5,75], [loadtest4,199], [loadtest5,26], [loadtest5,186], [loadtest5,196], [loadtest4,30]
```
```
/bin/kafka-topics.sh --zookeeper zk01.demo.com:2181,zk02.demo.com:2181,zk03.demo.com:2181/kafka --describe
Topic:_schemas PartitionCount:1 ReplicationFactor:3 Configs:cleanup.policy=compact
Topic: _schemas Partition: 0 Leader: 2 Replicas: 3,1,2 Isr: 2
Topic:loadtest2 PartitionCount:8 ReplicationFactor:2 Configs:
Topic: loadtest2 Partition: 0 Leader: 3 Replicas: 3,1 Isr: 3
Topic: loadtest2 Partition: 1 Leader: 3 Replicas: 1,3 Isr: 3
Topic: loadtest2 Partition: 2 Leader: 3 Replicas: 3,1 Isr: 3
Topic: loadtest2 Partition: 3 Leader: 3 Replicas: 1,3 Isr: 3
Topic: loadtest2 Partition: 4 Leader: 3 Replicas: 3,1 Isr: 3
Topic: loadtest2 Partition: 5 Leader: 3 Replicas: 1,3 Isr: 3
Topic: loadtest2 Partition: 6 Leader: 3 Replicas: 3,1 Isr: 3
```

CORS need to be enabled:

#### To view schema:

``` 
docker run --rm -p 8000:8000 -e "SCHEMAREGISTRY_URL=http://schema-registry.demo.com" landoop/schema-registry-ui 
```

#### To view topics: 

``` 
docker run --rm -it -p 8000:8000  \
           -e "KAFKA_REST_PROXY_URL=http://qa-kafka-rest.services.demo.com" \
           -e "PROXY=true" \
           landoop/kafka-topics-ui
```

#### Produce and Consume AVRO messages(/Users/vtomar/Downloads/kafka_conf/confluent-3.3.0/bin):

#### Produce dummy messages
```
./kafka-avro-console-producer --broker-list demo.kafka:9092 --topic demo_topic --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"f1","type":"string"}]}' --property schema.registry.url=htttp://schema-registry.demo.com:8081
```

#### Consume dummy messages
```
./kafka-avro-console-consumer --topic demo_topic --zookeeper zk.demo.com:2181/kafka --from-beginning --property schema.registry.url=htttp://schema-registry.demo.com:8081
```

#### Start landoop
```
docker run --rm -it -p 8000:8000 \
           -e "KAFKA_REST_PROXY_URL=http://kafka-rest.services.demo.com" \
           -e "PROXY=true" \
           landoop/kafka-topics-ui
```
#### 
```
/bin/kafka-producer-perf-test.sh --topic demo_topic \
--num-records 150000 \
--record-size 100000 \
--throughput 25000 \
--producer-props \
acks=-1 \
bootstrap.servers=kafka.demo.com:9092 \
buffer.memory=67108864 \
compression.type=lz4 \
batch.size=8196
```
#### 
```
/bin/kafka-producer-perf-test.sh --topic demo_topic \
--num-records 15000 \
--record-size 100 \
--throughput 2000 \
--producer-props \
acks=-1 \
bootstrap.servers=demo_kafka:9092 \
buffer.memory=67108864 \
batch.size=8196

rmr /kafka/brokers/topics
rmr /kafka/admin/delete_topics
rmr /kafka/config/topics
```
```
 cd $CONFLUENT_HOME
$ mkdir -p var
$ export CONFLUENT_CURRENT=${CONFLUENT_HOME}/var
$ confluent current
```
From <https://github.com/confluentinc/confluent-cli> 

#### Schema-registry
```
/bin/kafka-topics.sh --zookeeper  zk.demo.com:2181/kafka --list >> /tmp/topics_list
for i in `cat /tmp/topics_list`; do 
/bin/kafka-topics.sh --zookeeper zk.demo.com:2181/kafka --alter --topic $i --config retention.ms=604800000; done
```

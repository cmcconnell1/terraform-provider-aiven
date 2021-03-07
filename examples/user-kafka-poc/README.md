# Aiven Kafka Quickstart Demo

### Overview
- Aiven is a Database as a Service vendor.  In this document we demonstrate how you could go about creating the requisite Aiven account/environment and a sample kafka application that uses Aiven services. 
- Note that after testing you can also turn off the services and they will stop consuming credits. They can then be turned back on as needed.


### Tutorial
- The goals of this simple User POC/demo is to provide a Demo Application that sends JSON data to our Aiven cloud environment which can be just simple code snippets (or a more sophisticated application in any desired language) that send mock data to our Aiven cloud environment.

### Requirements
- [Aiven account created](https://console.aiven.io/signup) with sufficient demo credits (granted for new user accounts).
- [Aiven API token](https://console.aiven.io/profile/auth) generated from within and for your account.

- [Terraform](https://www.terraform.io/downloads.html) version 13.x or later installed on your workstation.

##### Recommendations
- [tfenv](https://github.com/tfutils/tfenv) is recommended to manage multiple terraform versions in projects, etc.
    - see how we can dynamically add/set/change terraform versions with tfenv as shown below.

##### References
- [Aiven Terraform Provider Docs](https://registry.terraform.io/providers/aiven/aiven/latest/docs)

##### Part-1 [Getting Started with Aiven Kafka](https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka)

Here we create a Kafka service within the hosted Aiven environment and we provide a simple code snippet/script (feel free to swap out our simple demo code with you preferred alternative) that produces valid JSON data to a topic in our hosted Aiven Kafka service. 

- Mock JSON data
  - Our example the mock data __ideally__ uses a __key__ (which should be a valid JSON string) containing a random __id__, (i.e.: __UUID__)
The message payload _should_ be a valid JSON object. The payload could be a mock _event_ from an interesting use case--i.e.: IoT sensor, stock tickets, or financial transactions. 
The event could include a timestamp represented by a string with the date in ISO 8601 format. 

- The producer’s data will be readable from the Aiven web console from the Kafka service (which can be accesses): 
  - View => 
    - Topics => 
      - Topic Name => 
        - Fetch Messages (Format: json)  
          - Integrations - Observability and Monitoring


Part-2 [Enable integrations to gather metrics from your Kafka service](https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana)
- Here we configure integrations to be: 
      - Kafka => 
        - InfluxDB => 
          - Grafana



## TL;DR Steps to deploy Aiven user POC environment

- Please register to create an account on [Aiven](https://console.aiven.io/signup.html) 
- Upon registratino of a valid new account your account will be given $300 worth of credits to test and validate Aiven hosted solutions. 

- add your token to the `avn_api_token` variable in your `terraform.auto.tfvars` file.

- Configure the Aiven Terraform provider version 
  - update `main.tf` with the [latest release/version](https://github.com/aiven/terraform-provider-aiven/releases/latest) i.e.:
    - "2.1.7" and as is set here:

    ```console
    cd examples/user-kafka-poc
    egrep -A 1 'source = "aiven/aiven"' main.tf
    source = "aiven/aiven"
    version = "2.1.7"
    ```
- Update the `terraform.auto.tfvars` file with your values for:
    - `aiven_api_token` 
    - `aiven_project_name`


##### Deploy IAC Terraform to Aiven Environment
- Install and configure desired/required version of Terraform for our tutorial (i.e.: 0.13.5)
```console
alias tf='/usr/local/bin/terraform'
tfenv install 0.13.5
tfenv use 0.13.5
echo "0.13.5" > ./.terrform-version
tf init
tf plan
tf apply # [-auto-approve]
```
- We can watch in the [Aiven API console](https://console.aiven.io/project/senior-b7bb/services) as our infrastructure is deployed
![Example Aiven Console Screenshot during Terraform Apply](../../images/aiven-console-terraform-applying.jpg?raw=true)

- upon completion of the deployment of the `tf apply` command, the normal terraform options can be used:
  - show the terraform resources deployed: `tf show`
  - create a graph of the terraform resources deployed: `tf graph | dot -Tsvg > ../../images/user-kafka-poc.svg`
  - example graph can be viewed with a browser()
  - ![Example Terraform Graph](../../images/user-kafka-poc_svg.jpg?raw=true)

##### Example Python Application
- Reference Docs
  - [Getting Started with Aiven Kafka](https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka)
  - [Aiven Examples Kafka Python](https://github.com/aiven/aiven-examples/tree/master/kafka/python)

- Using Kafkacat
```console
cat kafkacat.config
bootstrap.servers=samplekafka-senior-b7bb.aivencloud.com:26096
security.protocol=ssl
ssl.key.location=/Users/cmcc/work/aiven/kafkaCerts/service.key
ssl.certificate.location=/Users/cmcc/work/aiven/kafkaCerts/service.cert
ssl.ca.location=/Users/cmcc/work/aiven/kafkaCerts/ca.pem
```
- TODO: fix this
```console
kafkacat -F kafkacat.config -t demo-topic
% Reading configuration from file kafkacat.config
% Auto-selecting Consumer mode (use -P or -C to override)
% ERROR: Failed to query metadata for topic demo-topic: Local: Broker transport failure
```

- TODO fix this all connectivity issues sad panda

set timeout per kafka-python docs getting nice error: `kafka.errors.NoBrokersAvailable: NoBrokersAvailable`
```console
./python-kafka-producer.py
Traceback (most recent call last):
  File "/Users/cmcc/development/terraform-provider-aiven/examples/user-kafka-poc/bin/./python-kafka-producer.py", line 10, in <module>
    producer = KafkaProducer(
  File "/usr/local/lib/python3.9/site-packages/kafka/producer/kafka.py", line 381, in __init__
    client = KafkaClient(metrics=self._metrics, metric_group_prefix='producer',
  File "/usr/local/lib/python3.9/site-packages/kafka/client_async.py", line 244, in __init__
    self.config['api_version'] = self.check_version(timeout=check_timeout)
  File "/usr/local/lib/python3.9/site-packages/kafka/client_async.py", line 927, in check_version
    raise Errors.NoBrokersAvailable()
kafka.errors.NoBrokersAvailable: NoBrokersAvailable
```

- Tried yet another method but stil no love--using the official Aiven python example code / doc
  - launch a wrapper script that will validate our ability to connect to our hosted kafka service and produce kafka messages into our demo-topic
```console
cd bin/aiven-examples-tree-master-kafka-python && ./wrapper.sh
```
```console
./main.py --service-uri samplekafka-senior-b7bb.aivencloud.com:26096 --ca-path ~/work/aiven/kafkaCerts/ca.pem --key-path ~/work/aiven/kafkaCerts/service.key --cert-path ~/work/aiven/kafkaCerts/service.cert --producer
<SNIP>
kafka.errors.NoBrokersAvailable: NoBrokersAvailable
```

##### Aiven Grafana
- Login to the project Grafana instance
- Note that per the Aiven docs here:  https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana
  - Logging in with the user credentials specified https://console.aiven.io/project/senior-b7bb/services/samplegrafana/overview


##### Mock JSON data 
- TODO: find ISO 8601 complaint demo JSON mock data...
- for now just created something located in `./test` from https://www.mockaroo.com

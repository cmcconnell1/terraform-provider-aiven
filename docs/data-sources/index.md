---
layout: default
title: Datasources Schema
nav_order: 2
---
## Data-sources 
### aiven_account_team 
#### Required 
* **account_id** _Account id_ 
* **name** _Account team name_ 
##### Computed 
* **update_time** _Time of last update_ 
* **id**  
* **team_id** _Account team id_ 
* **create_time** _Time of creation_ 
### aiven_kafka_acl 
#### Required 
* **topic** _Topic name pattern for the ACL entry_ 
* **service_name** _Service to link the Kafka ACL to_ 
* **project** _Project to link the Kafka ACL to_ 
* **username** _Username pattern for the ACL entry_ 
#### Optional 
* **permission** _Kafka permission to grant (admin, read, readwrite, write)_ 
##### Computed 
* **id**  
### aiven_project_user 
#### Required 
* **email** _Email address of the user_ 
* **project** _The project the user belongs to_ 
#### Optional 
* **member_type** _Project membership type. One of: admin, developer, operator_ 
##### Computed 
* **id**  
* **accepted** _Whether the user has accepted project membership or not_ 
### aiven_connection_pool 
#### Required 
* **project** _Project to link the connection pool to_ 
* **service_name** _Service to link the connection pool to_ 
* **pool_name** _Name of the pool_ 
#### Optional 
* **pool_mode** _Mode the pool operates in (session, transaction, statement)_ 
* **username** _Name of the service user used to connect to the database_ 
* **database_name** _Name of the database the pool connects to_ 
* **pool_size** _Number of connections the pool may create towards the backend server_ 
##### Computed 
* **id**  
* **connection_uri** _URI for connecting to the pool_ 
### aiven_kafka_topic 
#### Required 
* **topic_name** _Topic name_ 
* **service_name** _Service to link the kafka topic to_ 
* **project** _Project to link the kafka topic to_ 
#### Optional 
* **replication** _Replication factor for the topic_ 
* **retention_bytes** _Retention bytes_ 
* **cleanup_policy** _Topic cleanup policy. Allowed values: delete, compact_ 
* **retention_hours** _Retention period (hours)_ 
* **partitions** _Number of partitions to create in the topic_ 
* **termination_protection** _It is a Terraform client-side deletion protection, which prevents a Kafka 
			topic from being deleted. It is recommended to enable this for any production Kafka 
			topic containing critical data._ 
* **minimum_in_sync_replicas** _Minimum required nodes in-sync replicas (ISR) to produce to a partition_ 
##### Computed 
* **id**  
### aiven_project 
#### Required 
* **project** _Project name_ 
#### Optional 
* **technical_emails** _Technical contact emails of the project_ 
* **copy_from_project** _Copy properties from another project. Only has effect when a new project is created._ 
* **country_code** _Billing country code of the project_ 
* **account_id** _Account ID_ 
* **billing_emails** _Billing contact emails of the project_ 
* **card_id** _Credit card ID_ 
* **billing_address** _Billing name and address of the project_ 
##### Computed 
* **id**  
* **ca_cert** _Project root CA. This is used by some services like Kafka to sign service certificate_ 
### aiven_kafka_schema_configuration 
#### Required 
* **project** _Project to link the Kafka Schema to_ 
* **service_name** _Service to link the Kafka Schema to_ 
#### Optional 
* **subject_name** _Kafka Schema Subject name_ 
* **schema** _Kafka Schema configuration should be a valid Avro Schema JSON format_ 
##### Computed 
* **version** _Kafka Schema configuration version_ 
* **id**  
### aiven_kafka_connector 
#### Required 
* **project** _Project to link the kafka connector to_ 
* **connector_name** _Kafka connector name_ 
* **service_name** _Service to link the kafka connector to_ 
#### Optional 
* **config** _Kafka Connector configuration parameters_ 
##### Computed 
* **plugin_version** _Kafka connector version_ 
* **plugin_doc_url** _Kafka connector documentation URL_ 
* **id**  
* **plugin_author** _Kafka connector author_ 
* **plugin_class** _Kafka connector Java class_ 
* **plugin_type** _Kafka connector type_ 
* **plugin_title** _Kafka connector title_ 
### aiven_account_team_project 
#### Required 
* **team_id** _Account team id_ 
* **project_name** _Account team project name_ 
* **account_id** _Account id_ 
#### Optional 
* **team_type** _Account team project type, can one of the following values: admin, developer, operator and read_only_ 
##### Computed 
* **id**  
### aiven_kafka_schema 
#### Required 
* **subject_name** _Kafka Schema Subject name_ 
* **project** _Project to link the Kafka Schema to_ 
* **service_name** _Service to link the Kafka Schema to_ 
#### Optional 
* **schema** _Kafka Schema configuration should be a valid Avro Schema JSON format_ 
##### Computed 
* **version** _Kafka Schema configuration version_ 
* **id**  
### aiven_account_team_member 
#### Required 
* **account_id** _Account id_ 
* **user_email** _Team invite user email_ 
* **team_id** _Account team id_ 
##### Computed 
* **id**  
* **accepted** _Team member invitation status_ 
* **invited_by_user_email** _Team invited by user email_ 
* **create_time** _Time of creation_ 
### aiven_service_user 
#### Required 
* **service_name** _Service to link the user to_ 
* **project** _Project to link the user to_ 
* **username** _Name of the user account_ 
##### Computed 
* **id**  
* **access_key** _Access certificate key for the user if applicable for the service in question_ 
* **type** _Type of the user account_ 
* **password** _Password of the user_ 
* **access_cert** _Access certificate for the user if applicable for the service in question_ 
### aiven_account 
#### Required 
* **name** _Account name_ 
##### Computed 
* **update_time** _Time of last update_ 
* **id**  
* **tenant_id** _Tenant id_ 
* **account_id** _Account id_ 
* **owner_team_id** _Owner team id_ 
* **create_time** _Time of creation_ 
### aiven_elasticsearch_acl 
#### Required 
* **service_name** _Service to link the Elasticsearch ACLs to_ 
* **project** _Project to link the Elasticsearch ACLs to_ 
#### Optional 
* **extended_acl** _Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target indexes they have been granted access to_ 
* **enabled** _Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access_ 
##### Computed 
* **id**  
### aiven_project_vpc 
#### Required 
* **project** _The project the VPC belongs to_ 
* **cloud_name** _Cloud the VPC is in_ 
#### Optional 
* **network_cidr** _Network address range used by the VPC like 192.168.0.0/24_ 
##### Computed 
* **id**  
* **state** _State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)_ 
### aiven_vpc_peering_connection 
#### Required 
* **vpc_id** _The VPC the peering connection belongs to_ 
* **peer_vpc** _AWS VPC ID or GCP VPC network name of the peered VPC_ 
* **peer_cloud_account** _AWS account ID or GCP project ID of the peered VPC_ 
#### Optional 
* **peer_region** _AWS region of the peered VPC (if not in the same region as Aiven VPC)_ 
##### Computed 
* **state_info** _State-specific help or error information_ 
* **id**  
* **peering_connection_id** _Cloud provider identifier for the peering connection if available_ 
* **state** _State of the peering connection_ 
### aiven_database 
#### Required 
* **database_name** _Service database name_ 
* **project** _Project to link the database to_ 
* **service_name** _Service to link the database to_ 
#### Optional 
* **lc_ctype** _Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8_ 
* **lc_collate** _Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8_ 
* **termination_protection** _It is a Terraform client-side deletion protections, which prevents the database
			from being deleted by Terraform. It is recommended to enable this for any production
			databases containing critical data._ 
##### Computed 
* **id**  
### aiven_service_integration_endpoint 
#### Required 
* **project** _Project the service integration endpoint belongs to_ 
* **endpoint_name** _Name of the service integration endpoint_ 
#### Optional 
* **endpoint_type** _Type of the service integration endpoint_ 
##### Computed 
* **id**  
* **endpoint_config** _Integration endpoint specific backend configuration_ 
### aiven_service 
#### Required 
* **service_name** _Service name_ 
* **project** _Target project_ 
#### Optional 
* **service_type** _Service type code_ 
* **cloud_name** _Cloud the service runs in_ 
* **plan** _Subscription plan_ 
* **maintenance_window_time** _Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format._ 
* **project_vpc_id** _Identifier of the VPC the service should be in, if any_ 
* **termination_protection** _Prevent service from being deleted. It is recommended to have this enabled for all services._ 
* **maintenance_window_dow** _Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc._ 
##### Computed 
* **service_uri** _URI for connecting to the service. Service specific info is under "kafka", "pg", etc._ 
* **service_host** _Service hostname_ 
* **service_password** _Password used for connecting to the service, if applicable_ 
* **service_username** _Username used for connecting to the service, if applicable_ 
* **id**  
* **service_port** _Service port_ 
* **state** _Service state_ 


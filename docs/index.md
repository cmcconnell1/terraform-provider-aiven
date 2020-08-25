---
layout: default
title: Provider Schema
nav_order: 1
---
## Resources 
### aiven_database 
#### Required 
* **service_name** _Service to link the database to_ 
* **project** _Project to link the database to_ 
* **database_name** _Service database name_ 
#### Optional 
* **lc_ctype** _Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8_ 
* **termination_protection** _It is a Terraform client-side deletion protections, which prevents the database
			from being deleted by Terraform. It is recommended to enable this for any production
			databases containing critical data._ 
* **lc_collate** _Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8_ 
##### Computed 
* **id**  
### aiven_project_vpc 
#### Required 
* **cloud_name** _Cloud the VPC is in_ 
* **project** _The project the VPC belongs to_ 
* **network_cidr** _Network address range used by the VPC like 192.168.0.0/24_ 
##### Computed 
* **state** _State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)_ 
* **id**  
### aiven_kafka_acl 
#### Required 
* **permission** _Kafka permission to grant (admin, read, readwrite, write)_ 
* **username** _Username pattern for the ACL entry_ 
* **service_name** _Service to link the Kafka ACL to_ 
* **topic** _Topic name pattern for the ACL entry_ 
* **project** _Project to link the Kafka ACL to_ 
##### Computed 
* **id**  
### aiven_account_team 
#### Required 
* **name** _Account team name_ 
* **account_id** _Account id_ 
##### Computed 
* **team_id** _Account team id_ 
* **id**  
* **update_time** _Time of last update_ 
* **create_time** _Time of creation_ 
### aiven_project 
#### Required 
* **project** _Project name_ 
#### Optional 
* **card_id** _Credit card ID_ 
* **technical_emails** _Technical contact emails of the project_ 
* **copy_from_project** _Copy properties from another project. Only has effect when a new project is created._ 
* **account_id** _Account ID_ 
* **country_code** _Billing country code of the project_ 
* **billing_address** _Billing name and address of the project_ 
* **billing_emails** _Billing contact emails of the project_ 
##### Computed 
* **ca_cert** _Project root CA. This is used by some services like Kafka to sign service certificate_ 
* **id**  
### aiven_account 
#### Required 
* **name** _Account name_ 
##### Computed 
* **tenant_id** _Tenant id_ 
* **id**  
* **owner_team_id** _Owner team id_ 
* **account_id** _Account id_ 
* **update_time** _Time of last update_ 
* **create_time** _Time of creation_ 
### aiven_service_user 
#### Required 
* **username** _Name of the user account_ 
* **service_name** _Service to link the user to_ 
* **project** _Project to link the user to_ 
##### Computed 
* **access_key** _Access certificate key for the user if applicable for the service in question_ 
* **access_cert** _Access certificate for the user if applicable for the service in question_ 
* **id**  
* **password** _Password of the user_ 
* **type** _Type of the user account_ 
### aiven_service_integration_endpoint 
#### Required 
* **project** _Project the service integration endpoint belongs to_ 
* **endpoint_type** _Type of the service integration endpoint_ 
* **endpoint_name** _Name of the service integration endpoint_ 
##### Computed 
* **endpoint_config** _Integration endpoint specific backend configuration_ 
* **id**  
### aiven_kafka_connector 
#### Required 
* **service_name** _Service to link the kafka connector to_ 
* **connector_name** _Kafka connector name_ 
* **config** _Kafka Connector configuration parameters_ 
* **project** _Project to link the kafka connector to_ 
##### Computed 
* **plugin_title** _Kafka connector title_ 
* **plugin_class** _Kafka connector Java class_ 
* **task** _List of tasks of a connector_ 
* **plugin_author** _Kafka connector author_ 
* **plugin_type** _Kafka connector type_ 
* **plugin_version** _Kafka connector version_ 
* **id**  
* **plugin_doc_url** _Kafka connector documentation URL_ 
### aiven_kafka_schema 
#### Required 
* **subject_name** _Kafka Schema Subject name_ 
* **service_name** _Service to link the Kafka Schema to_ 
* **project** _Project to link the Kafka Schema to_ 
* **schema** _Kafka Schema configuration should be a valid Avro Schema JSON format_ 
##### Computed 
* **id**  
* **version** _Kafka Schema configuration version_ 
### aiven_kafka_topic 
#### Required 
* **service_name** _Service to link the kafka topic to_ 
* **project** _Project to link the kafka topic to_ 
* **replication** _Replication factor for the topic_ 
* **topic_name** _Topic name_ 
* **partitions** _Number of partitions to create in the topic_ 
#### Optional 
* **minimum_in_sync_replicas** _Minimum required nodes in-sync replicas (ISR) to produce to a partition_ 
* **retention_bytes** _Retention bytes_ 
* **retention_hours** _Retention period (hours)_ 
* **cleanup_policy** _Topic cleanup policy. Allowed values: delete, compact_ 
* **termination_protection** _It is a Terraform client-side deletion protection, which prevents a Kafka 
			topic from being deleted. It is recommended to enable this for any production Kafka 
			topic containing critical data._ 
##### Computed 
* **id**  
### aiven_service 
#### Required 
* **service_name** _Service name_ 
* **service_type** _Service type code_ 
* **project** _Target project_ 
#### Optional 
* **maintenance_window_dow** _Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc._ 
* **project_vpc_id** _Identifier of the VPC the service should be in, if any_ 
* **maintenance_window_time** _Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format._ 
* **termination_protection** _Prevent service from being deleted. It is recommended to have this enabled for all services._ 
* **plan** _Subscription plan_ 
* **cloud_name** _Cloud the service runs in_ 
##### Computed 
* **service_username** _Username used for connecting to the service, if applicable_ 
* **service_host** _Service hostname_ 
* **service_password** _Password used for connecting to the service, if applicable_ 
* **service_uri** _URI for connecting to the service. Service specific info is under "kafka", "pg", etc._ 
* **service_port** _Service port_ 
* **components** _Service component information objects_ 
* **id**  
* **state** _Service state_ 
### aiven_connection_pool 
#### Required 
* **username** _Name of the service user used to connect to the database_ 
* **service_name** _Service to link the connection pool to_ 
* **project** _Project to link the connection pool to_ 
* **database_name** _Name of the database the pool connects to_ 
* **pool_name** _Name of the pool_ 
#### Optional 
* **pool_mode** _Mode the pool operates in (session, transaction, statement)_ 
* **pool_size** _Number of connections the pool may create towards the backend server_ 
##### Computed 
* **id**  
* **connection_uri** _URI for connecting to the pool_ 
### aiven_project_user 
#### Required 
* **project** _The project the user belongs to_ 
* **member_type** _Project membership type. One of: admin, developer, operator_ 
* **email** _Email address of the user_ 
##### Computed 
* **accepted** _Whether the user has accepted project membership or not_ 
* **id**  
### aiven_kafka_schema_configuration 
#### Required 
* **project** _Project to link the Kafka Schemas Configuration to_ 
* **compatibility_level** _Kafka Schemas compatibility level_ 
* **service_name** _Service to link the Kafka Schemas Configuration to_ 
##### Computed 
* **id**  
### aiven_elasticsearch_acl 
#### Required 
* **project** _Project to link the Elasticsearch ACLs to_ 
* **service_name** _Service to link the Elasticsearch ACLs to_ 
#### Optional 
* **extended_acl** _Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target indexes they have been granted access to_ 
* **enabled** _Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access_ 
##### Computed 
* **id**  
### aiven_account_team_member 
#### Required 
* **account_id** _Account id_ 
* **team_id** _Account team id_ 
* **user_email** _Team invite user email_ 
##### Computed 
* **id**  
* **accepted** _Team member invitation status_ 
* **invited_by_user_email** _Team invited by user email_ 
* **create_time** _Time of creation_ 
### aiven_account_team_project 
#### Required 
* **account_id** _Account id_ 
* **team_id** _Account team id_ 
#### Optional 
* **project_name** _Account team project name_ 
* **team_type** _Account team project type, can one of the following values: admin, developer, operator and read_only_ 
##### Computed 
* **id**  
### aiven_vpc_peering_connection 
#### Required 
* **vpc_id** _The VPC the peering connection belongs to_ 
* **peer_vpc** _AWS VPC ID or GCP VPC network name of the peered VPC_ 
* **peer_cloud_account** _AWS account ID or GCP project ID of the peered VPC_ 
#### Optional 
* **peer_region** _AWS region of the peered VPC (if not in the same region as Aiven VPC)_ 
##### Computed 
* **peering_connection_id** _Cloud provider identifier for the peering connection if available_ 
* **id**  
* **state_info** _State-specific help or error information_ 
* **state** _State of the peering connection_ 
### aiven_service_integration 
#### Required 
* **project** _Project the integration belongs to_ 
* **integration_type** _Type of the service integration_ 
#### Optional 
* **source_service_name** _Source service for the integration (if any)_ 
* **destination_service_name** _Destination service for the integration (if any)_ 
* **destination_endpoint_id** _Destination endpoint for the integration (if any)_ 
* **source_endpoint_id** _Source endpoint for the integration (if any)_ 
##### Computed 
* **id**  
--- 
## Data-sources 
### aiven_database 
#### Required 
* **service_name** _Service to link the database to_ 
* **project** _Project to link the database to_ 
* **database_name** _Service database name_ 
#### Optional 
* **lc_ctype** _Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8_ 
* **termination_protection** _It is a Terraform client-side deletion protections, which prevents the database
			from being deleted by Terraform. It is recommended to enable this for any production
			databases containing critical data._ 
* **lc_collate** _Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8_ 
##### Computed 
* **id**  
### aiven_project_vpc 
#### Required 
* **cloud_name** _Cloud the VPC is in_ 
* **project** _The project the VPC belongs to_ 
#### Optional 
* **network_cidr** _Network address range used by the VPC like 192.168.0.0/24_ 
##### Computed 
* **state** _State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)_ 
* **id**  
### aiven_kafka_acl 
#### Required 
* **username** _Username pattern for the ACL entry_ 
* **service_name** _Service to link the Kafka ACL to_ 
* **topic** _Topic name pattern for the ACL entry_ 
* **project** _Project to link the Kafka ACL to_ 
#### Optional 
* **permission** _Kafka permission to grant (admin, read, readwrite, write)_ 
##### Computed 
* **id**  
### aiven_account_team 
#### Required 
* **name** _Account team name_ 
* **account_id** _Account id_ 
##### Computed 
* **team_id** _Account team id_ 
* **id**  
* **update_time** _Time of last update_ 
* **create_time** _Time of creation_ 
### aiven_project 
#### Required 
* **project** _Project name_ 
#### Optional 
* **card_id** _Credit card ID_ 
* **technical_emails** _Technical contact emails of the project_ 
* **copy_from_project** _Copy properties from another project. Only has effect when a new project is created._ 
* **account_id** _Account ID_ 
* **country_code** _Billing country code of the project_ 
* **billing_address** _Billing name and address of the project_ 
* **billing_emails** _Billing contact emails of the project_ 
##### Computed 
* **ca_cert** _Project root CA. This is used by some services like Kafka to sign service certificate_ 
* **id**  
### aiven_account 
#### Required 
* **name** _Account name_ 
##### Computed 
* **tenant_id** _Tenant id_ 
* **id**  
* **owner_team_id** _Owner team id_ 
* **account_id** _Account id_ 
* **update_time** _Time of last update_ 
* **create_time** _Time of creation_ 
### aiven_service_user 
#### Required 
* **username** _Name of the user account_ 
* **service_name** _Service to link the user to_ 
* **project** _Project to link the user to_ 
##### Computed 
* **access_key** _Access certificate key for the user if applicable for the service in question_ 
* **access_cert** _Access certificate for the user if applicable for the service in question_ 
* **id**  
* **password** _Password of the user_ 
* **type** _Type of the user account_ 
### aiven_service_integration_endpoint 
#### Required 
* **project** _Project the service integration endpoint belongs to_ 
* **endpoint_name** _Name of the service integration endpoint_ 
#### Optional 
* **endpoint_type** _Type of the service integration endpoint_ 
##### Computed 
* **endpoint_config** _Integration endpoint specific backend configuration_ 
* **id**  
### aiven_kafka_connector 
#### Required 
* **service_name** _Service to link the kafka connector to_ 
* **connector_name** _Kafka connector name_ 
* **project** _Project to link the kafka connector to_ 
#### Optional 
* **config** _Kafka Connector configuration parameters_ 
##### Computed 
* **plugin_doc_url** _Kafka connector documentation URL_ 
* **plugin_class** _Kafka connector Java class_ 
* **id**  
* **plugin_title** _Kafka connector title_ 
* **plugin_author** _Kafka connector author_ 
* **plugin_type** _Kafka connector type_ 
* **plugin_version** _Kafka connector version_ 
### aiven_kafka_schema 
#### Required 
* **subject_name** _Kafka Schema Subject name_ 
* **service_name** _Service to link the Kafka Schema to_ 
* **project** _Project to link the Kafka Schema to_ 
#### Optional 
* **schema** _Kafka Schema configuration should be a valid Avro Schema JSON format_ 
##### Computed 
* **id**  
* **version** _Kafka Schema configuration version_ 
### aiven_kafka_topic 
#### Required 
* **service_name** _Service to link the kafka topic to_ 
* **project** _Project to link the kafka topic to_ 
* **topic_name** _Topic name_ 
#### Optional 
* **minimum_in_sync_replicas** _Minimum required nodes in-sync replicas (ISR) to produce to a partition_ 
* **retention_bytes** _Retention bytes_ 
* **retention_hours** _Retention period (hours)_ 
* **cleanup_policy** _Topic cleanup policy. Allowed values: delete, compact_ 
* **termination_protection** _It is a Terraform client-side deletion protection, which prevents a Kafka 
			topic from being deleted. It is recommended to enable this for any production Kafka 
			topic containing critical data._ 
* **replication** _Replication factor for the topic_ 
* **partitions** _Number of partitions to create in the topic_ 
##### Computed 
* **id**  
### aiven_service 
#### Required 
* **service_name** _Service name_ 
* **project** _Target project_ 
#### Optional 
* **maintenance_window_dow** _Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc._ 
* **project_vpc_id** _Identifier of the VPC the service should be in, if any_ 
* **maintenance_window_time** _Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format._ 
* **termination_protection** _Prevent service from being deleted. It is recommended to have this enabled for all services._ 
* **plan** _Subscription plan_ 
* **service_type** _Service type code_ 
* **cloud_name** _Cloud the service runs in_ 
##### Computed 
* **service_username** _Username used for connecting to the service, if applicable_ 
* **service_password** _Password used for connecting to the service, if applicable_ 
* **service_uri** _URI for connecting to the service. Service specific info is under "kafka", "pg", etc._ 
* **service_port** _Service port_ 
* **service_host** _Service hostname_ 
* **state** _Service state_ 
* **id**  
### aiven_connection_pool 
#### Required 
* **service_name** _Service to link the connection pool to_ 
* **project** _Project to link the connection pool to_ 
* **pool_name** _Name of the pool_ 
#### Optional 
* **username** _Name of the service user used to connect to the database_ 
* **database_name** _Name of the database the pool connects to_ 
* **pool_mode** _Mode the pool operates in (session, transaction, statement)_ 
* **pool_size** _Number of connections the pool may create towards the backend server_ 
##### Computed 
* **id**  
* **connection_uri** _URI for connecting to the pool_ 
### aiven_project_user 
#### Required 
* **project** _The project the user belongs to_ 
* **email** _Email address of the user_ 
#### Optional 
* **member_type** _Project membership type. One of: admin, developer, operator_ 
##### Computed 
* **accepted** _Whether the user has accepted project membership or not_ 
* **id**  
### aiven_kafka_schema_configuration 
#### Required 
* **service_name** _Service to link the Kafka Schema to_ 
* **project** _Project to link the Kafka Schema to_ 
#### Optional 
* **subject_name** _Kafka Schema Subject name_ 
* **schema** _Kafka Schema configuration should be a valid Avro Schema JSON format_ 
##### Computed 
* **id**  
* **version** _Kafka Schema configuration version_ 
### aiven_elasticsearch_acl 
#### Required 
* **project** _Project to link the Elasticsearch ACLs to_ 
* **service_name** _Service to link the Elasticsearch ACLs to_ 
#### Optional 
* **extended_acl** _Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target indexes they have been granted access to_ 
* **enabled** _Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access_ 
##### Computed 
* **id**  
### aiven_account_team_member 
#### Required 
* **account_id** _Account id_ 
* **team_id** _Account team id_ 
* **user_email** _Team invite user email_ 
##### Computed 
* **id**  
* **accepted** _Team member invitation status_ 
* **invited_by_user_email** _Team invited by user email_ 
* **create_time** _Time of creation_ 
### aiven_account_team_project 
#### Required 
* **account_id** _Account id_ 
* **project_name** _Account team project name_ 
* **team_id** _Account team id_ 
#### Optional 
* **team_type** _Account team project type, can one of the following values: admin, developer, operator and read_only_ 
##### Computed 
* **id**  
### aiven_vpc_peering_connection 
#### Required 
* **vpc_id** _The VPC the peering connection belongs to_ 
* **peer_vpc** _AWS VPC ID or GCP VPC network name of the peered VPC_ 
* **peer_cloud_account** _AWS account ID or GCP project ID of the peered VPC_ 
#### Optional 
* **peer_region** _AWS region of the peered VPC (if not in the same region as Aiven VPC)_ 
##### Computed 
* **peering_connection_id** _Cloud provider identifier for the peering connection if available_ 
* **id**  
* **state_info** _State-specific help or error information_ 
* **state** _State of the peering connection_ 


# Redis Data Source

The Redis data source provides information about the existing Aiven Redis service.

## Example Usage

```hcl
data "aiven_redis" "redis1" {
    project = data.aiven_project.pr1.project
    service_name = "my-redis1"
}
```

## Argument Reference

* `project` - (Required) identifies the project the service belongs to. To set up proper dependency
between the project and the service, refer to the project as shown in the above example.
Project cannot be changed later without destroying and re-creating the service.

* `service_name` - (Required) specifies the actual name of the service. The name cannot be changed
later without destroying and re-creating the service so name should be picked based on
intended service usage rather than current attributes.

## Attribute Reference

In addition to all arguments above, the following attributes are exported:

* `cloud_name` - defines where the cloud provider and region where the service is hosted
in. This can be changed freely after service is created. Changing the value will trigger
a potentially lengthy migration process for the service. Format is cloud provider name
(`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider
specific region name. These are documented on each Cloud provider's own support articles,
like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and
[here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).

* `plan` - defines what kind of computing resources are allocated for the service. It can
be changed after creation, though there are some restrictions when going to a smaller
plan such as the new plan must have sufficient amount of disk space to store all current
data and switching to a plan with fewer nodes might not be supported. The basic plan
names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is
(roughly) the amount of memory on each node (also other attributes like number of CPUs
and amount of disk space varies but naming is based on memory). The exact options can be
seen from the Aiven web console's Create Service dialog.

* `project_vpc_id` - optionally specifies the VPC the service should run in. If the value
is not set the service is not run inside a VPC. When set, the value should be given as a
reference as shown above to set up dependencies correctly and the VPC must be in the same
cloud and region as the service itself. Project can be freely moved to and from VPC after
creation but doing so triggers migration to new servers so the operation can take
significant amount of time to complete if the service has a lot of data.

* `termination_protection` - prevents the service from being deleted. It is recommended to
set this to `true` for all production services to prevent unintentional service
deletion. This does not shield against deleting databases or topics but for services
with backups much of the content can at least be restored from backup in case accidental
deletion is done.

* `maintenance_window_dow` - day of week when maintenance operations should be performed. 
On monday, tuesday, wednesday, etc.

* `maintenance_window_time` - time of day when maintenance operations should be performed. 
UTC time in HH:mm:ss format.

* `redis_user_config` - defines Redis specific additional configuration options. The following 
configuration options available:
    * `ip_filter` - Allow incoming connections from CIDR address block, e.g. `10.20.0.0/16`
    
    * `migration` - Migrate data from existing server
        * `dbname` - Database name for bootstrapping the initial connection
        * `host` - (Required) Hostname or IP address of the server where to migrate data from
        * `password` - Password for authentication with the server where to migrate data from
        * `port` - (Required) Port number of the server where to migrate data from
        * `ssl` - The server where to migrate data from is secured with SSL
        * `username` - User name for authentication with the server where to migrate data from
        * `ignore_dbs` - Comma-separated list of databases, which should be ignored during
        migration (supported by MySQL only at the moment)
    
    * `private_access` - Allow access to selected service ports from private networks
        * `prometheus` - Allow clients to connect to prometheus with a DNS name that always 
        resolves to the service's private IP addresses. Only available in certain network locations
        * `prometheus` - Allow clients to connect to redis with a DNS name that always 
        resolves to the service's private IP addresses. Only available in certain network locations
        
    * `public_access` - Allow access to selected service ports from the public Internet
        * `prometheus` - Allow clients to connect to prometheus from the public internet 
        for service nodes that are in a project VPC or another type of private network
        * `redis` - Allow clients to connect to redis from the public internet for service 
        nodes that are in a project VPC or another type of private network

    * `privatelink_access` - Allow access to selected service components through Privatelink
        * `redis` - Enable redis

    * `recovery_basebackup_name` - Name of the basebackup to restore in forked service
    * `redis_io_threads` - Redis IO thread count
    * `redis_lfu_decay_time"` - LFU maxmemory-policy counter decay time in minutes
    * `redis_lfu_log_factor` - Counter logarithm factor for volatile-lfu and allkeys-lfu 
    maxmemory-policies
    * `redis_maxmemory_policy` - Redis maxmemory-policy
    * `redis_notify_keyspace_events` - Set notify-keyspace-events option
    * `redis_ssl` - Require SSL to access Redis
    * `redis_timeout` - Redis idle connection timeout
    * `service_to_fork_from"` - Name of another service to fork from. This has effect only 
    when a new service is being created. 
    * `project_to_fork_from` - Name of another project to fork a service from. This has
    effect only when a new service is being created.

* `service_uri` - URI for connecting to the Redis service.

* `service_host` - Redis hostname.

* `service_port` - Redis port.

* `service_password` - Password used for connecting to the Redis service, if applicable.

* `service_username` - Username used for connecting to the Redis service, if applicable.

* `state` - Service state.

* `redis` - Redis specific server provided values.
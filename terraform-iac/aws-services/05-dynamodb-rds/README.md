# AWS Database Services: DynamoDB and Amazon RDS

AWS provides both managed NoSQL and relational database services. Choose according to the data model, access patterns, consistency and transaction needs, scale, and operational requirements rather than treating either service as a universal default.

## Amazon DynamoDB

### NoSQL model

Amazon DynamoDB is a fully managed, serverless NoSQL database supporting key-value and document data models. Tables are designed around access patterns and primary keys; a table does not require every item to have the same set of attributes.

### Tables, items, and attributes

- A **table** contains related data items.
- An **item** is an individual record, represented as a set of attributes.
- An **attribute** is a named value, such as a string, number, binary value, set, list, or map.

### Partition key and sort key

A **partition key** is the required primary-key component used to distribute data and locate items. A table may use a partition key alone (simple primary key) or a partition key together with a **sort key** (composite primary key). The sort key orders and groups items sharing the same partition-key value and supports range and prefix access patterns.

Good key design distributes traffic and supports known query patterns. A hot partition key can concentrate requests and limit throughput. Secondary indexes add alternate query patterns but consume storage and capacity and must be maintained.

### Common DynamoDB use cases

- User profiles, session state, shopping carts, and product catalogs.
- High-volume event, IoT, and gaming data.
- Applications needing low-latency key-based access at elastic scale.
- Serverless application backends and state stores.

Design the key schema and access patterns first; use transactions or indexes only where needed. Consider capacity mode, backups and point-in-time recovery, encryption, TTL behavior, and IAM access controls.

## Amazon RDS

### Relational database service

Amazon Relational Database Service (Amazon RDS) simplifies provisioning, patching, backups, monitoring, and recovery for relational database engines. RDS manages the database infrastructure, but customers remain responsible for schema, query design, access control, application behavior, and configuration choices.

### Supported engines

Amazon RDS supports managed deployments for engines including:

- Amazon Aurora (MySQL-compatible and PostgreSQL-compatible editions).
- PostgreSQL.
- MySQL.
- MariaDB.
- Oracle Database.
- Microsoft SQL Server.

Engine versions, features, editions, and Regions vary. Check current AWS documentation before selecting an engine or planning an upgrade.

### DB instances

A DB instance is a compute environment for an RDS database. It has a DB instance class, allocated storage, engine/version, network placement, security settings, and backup/maintenance configuration. RDS also offers deployment options such as Multi-AZ DB instances and, for supported engines and configurations, Multi-AZ DB clusters.

### Security

- Place databases in private subnets where practical and control access with VPC Security Groups.
- Use least-privilege database accounts and IAM controls where supported.
- Encrypt storage and backups; configure TLS for connections.
- Store credentials in AWS Secrets Manager or another approved secret store; rotate them where supported.
- Avoid publicly accessible database instances unless essential and narrowly controlled.
- Monitor audit and database logs and apply engine updates through a planned process.

### Backups

RDS automated backups support point-in-time recovery within the configured retention period, subject to engine and service constraints. Manual snapshots remain until deleted. Backups and snapshots may incur storage charges and are important for recovery; test restoration instead of assuming backups are usable.

### Multi-AZ

Multi-AZ deployments provide a high-availability standby or coordinated cluster deployment in another Availability Zone, depending on the deployment option and engine. They are designed for availability and failover, not as a general read-scaling mechanism. Failover can interrupt existing connections, so applications should reconnect safely.

### Read replicas

Read replicas copy data asynchronously for read scaling and, in some supported scenarios, disaster recovery. Replication lag can occur, so replicas may not immediately reflect the latest writes. Read replicas are not equivalent to a synchronous Multi-AZ standby.

### Common RDS use cases

- Applications requiring SQL, joins, relational constraints, or transactions.
- Existing applications built for a supported relational engine.
- Business systems such as order processing, inventory, and content management.
- Managed relational databases where the team wants to reduce infrastructure-maintenance work.

## Choosing between DynamoDB and RDS

Choose DynamoDB when access patterns are well-defined around keys, high-scale low-latency NoSQL access is desirable, and relational joins are not central. Choose RDS when a relational schema, SQL, joins, or engine compatibility are important. Consider data migration, consistency, transactions, operational skills, availability design, and cost before deciding.

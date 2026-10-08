# Amazon S3: Object Storage

## What is S3?

Amazon Simple Storage Service (Amazon S3) is a regional object-storage service. Data is stored as objects in buckets and accessed through AWS APIs, SDKs, or tools such as the AWS CLI. S3 is designed for high durability, but it is not a block device or a traditional mounted file system.

## Buckets and objects

- A **bucket** is a container for objects and is created in a selected AWS Region. General purpose bucket names are globally unique within an AWS partition.
- An **object** consists of data, a key (its name/path-like identifier), metadata, and optionally a version ID.
- Object keys are strings; slash-separated prefixes are naming conventions, not actual directories.

## Storage classes

Choose a class based on access frequency, retrieval latency, availability, minimum storage duration, and cost. Common classes include:

- **S3 Standard:** frequently accessed data.
- **S3 Intelligent-Tiering:** data with changing or unknown access patterns; monitoring and optional archive tiers have their own behavior and charges.
- **S3 Standard-IA / One Zone-IA:** infrequently accessed data with retrieval charges; One Zone-IA stores data in one Availability Zone.
- **S3 Express One Zone:** single-zone, high-performance access for supported use cases.
- **S3 Glacier Instant Retrieval:** archive data needing millisecond retrieval.
- **S3 Glacier Flexible Retrieval:** archive data with retrieval times ranging from minutes to hours.
- **S3 Glacier Deep Archive:** long-term archive with the lowest storage cost among these classes and longer restore times.

Minimum object-size, minimum storage-duration, retrieval, monitoring, and restore charges may apply. Confirm current regional pricing and class constraints before selecting one.

## Versioning

Bucket versioning preserves multiple versions of an object under the same key and helps recover from accidental overwrites or deletions. A delete in a versioned bucket usually creates a delete marker; previous versions remain until explicitly removed. Versioning increases storage use, so combine it with lifecycle rules and protection for important data.

## Lifecycle policies

Lifecycle rules can transition objects to lower-cost storage classes or expire current and noncurrent versions, incomplete multipart uploads, and delete markers according to a policy. Model retention and recovery requirements before adding expiration rules, and test rules on a limited prefix where possible.

## Encryption

S3 supports server-side encryption, including S3-managed keys (SSE-S3) and AWS Key Management Service keys (SSE-KMS). SSE-C lets a customer supply an encryption key for supported requests, which creates additional key-management responsibility. Client-side encryption encrypts data before it is sent to S3. Require encryption in transit (HTTPS) and choose key ownership and access controls appropriate to data sensitivity.

## Bucket policies and access control

A bucket policy is a resource-based IAM policy written in JSON. It can grant or deny access to principals and specify conditions. Access also depends on identity policies, Organizations guardrails, access points, ACL behavior where enabled, and other applicable controls. Enable S3 Block Public Access at the account and bucket levels unless public access is deliberately required and reviewed. Prefer IAM roles and narrowly scoped policies over public ACLs.

## Common use cases

- Static assets, application uploads, and backups.
- Data lakes, analytics, and machine-learning datasets.
- Logs, software packages, and build artifacts.
- Long-term archives and disaster-recovery copies.
- Static website content (with separate consideration for public access and HTTPS delivery through CloudFront).

## Security and operations checklist

- Block public access by default; review bucket and access-point policies.
- Use IAM roles and least privilege; avoid embedded credentials.
- Enable versioning and suitable retention for recovery requirements.
- Encrypt objects and use TLS for requests.
- Enable CloudTrail data events or S3 access logging where appropriate.
- Use lifecycle policies deliberately and monitor storage and request costs.
- Test restore and recovery procedures, including recovery from versioned deletes.

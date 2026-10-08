# Amazon EC2: Elastic Compute Cloud

## What is EC2?

Amazon Elastic Compute Cloud (EC2) provides resizable virtual machine instances. You choose an image, instance family and size, networking, storage, and access controls, then launch and manage the instance within an AWS Region and Availability Zone.

## AMIs

An Amazon Machine Image (AMI) is a template used to launch an instance. It specifies an operating system and may include software and configuration. AMIs are Region-specific; copy an AMI to another Region to launch it there. Use trusted, maintained images and patch the operating system and application after launch.

## Instance types

An instance type defines compute, memory, storage, and network characteristics. Families target different workloads:

- General purpose for balanced workloads.
- Compute optimized for CPU-intensive jobs.
- Memory optimized for memory-intensive databases or in-memory processing.
- Storage optimized for high local storage throughput or I/O.
- Accelerated computing for GPU or specialized accelerator workloads.

Choose based on measured workload needs, architecture, operating system, and price. Instance generation, availability, and supported features vary by Region.

## Key pairs

An EC2 key pair supplies a public key that can be used for operating-system login where the image and access method support it. The private key is sensitive and should be protected; AWS does not provide another copy of the private key after the initial download. Many environments should use AWS Systems Manager Session Manager or other controlled access methods instead of opening SSH broadly to the internet.

## Security Groups

A Security Group is a stateful virtual firewall attached to an instance's network interface. It has allow rules for inbound and outbound traffic; return traffic for an allowed connection is automatically permitted. Security Groups do not have explicit deny rules. Restrict sources, destinations, and ports to the minimum necessary—for example, allow administrative access only from a controlled network rather than `0.0.0.0/0`.

## EBS storage

Amazon Elastic Block Store (EBS) provides block storage volumes for EC2. EBS volumes are generally attached to an instance in the same Availability Zone and persist independently of the instance lifecycle according to their configuration. Choose volume type, size, and performance for the workload; enable encryption and backups/snapshots for important data. Instance-store disks are different: their data is ephemeral and tied to the host lifecycle.

## Public and private IP addresses

- A **private IPv4 address** is used for communication within connected private networks. It generally remains associated with the network interface while attached.
- A **public IPv4 address** can provide internet-routable addressing when the subnet routing and security rules also permit it. Auto-assigned public addresses may change after stop/start; Elastic IP addresses provide a separately allocated static public IPv4 address but incur charges under AWS pricing rules.

An address alone does not make an instance reachable. Routing, Internet Gateway/NAT design, Security Groups, network ACLs, host firewall, and application listener must all be considered.

## Instance lifecycle

Common EC2 instance states include:

- **Pending:** AWS is preparing the instance.
- **Running:** the instance is operating; compute charges generally accrue.
- **Stopping / Stopped:** a stop transition is in progress / the instance is shut down. EBS volumes generally persist; instance-store data does not.
- **Shutting-down / Terminated:** termination is in progress / the instance is permanently removed. EBS deletion depends on volume settings.

Reboot, stop/start, and termination have different effects on host placement, public addressing, and data. Review termination protection and storage deletion settings before destructive actions.

## Common use cases

- Hosting web applications, APIs, and background workers.
- Running development, testing, or legacy workloads requiring OS-level control.
- Batch processing and temporary compute.
- Self-managed databases or specialized software when managed services are unsuitable.
- Building custom AMIs for repeatable server fleets.

## Operational considerations

Use instance profiles for AWS API access rather than static access keys on a VM. Patch and monitor the OS, use least-privilege network rules, encrypt storage, back up critical data, and review scaling and cost. Consider managed alternatives such as ECS, EKS, Lambda, or managed databases where they better fit operational needs.

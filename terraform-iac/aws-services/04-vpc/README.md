# Amazon VPC: Virtual Private Cloud

## What is a VPC?

Amazon Virtual Private Cloud (VPC) provides logically isolated networking for AWS resources. A VPC is created in one Region and can span multiple Availability Zones in that Region. Subnets are each associated with one Availability Zone. Routing, gateways, firewalls, DNS settings, and address ranges determine how resources communicate.

## CIDR

A VPC is assigned one or more IPv4 CIDR blocks and may also have IPv6 CIDR blocks. CIDR notation describes an address range, such as `10.0.0.0/16`. Plan ranges to avoid overlap with on-premises networks, peered VPCs, and other connected networks. Subnet CIDR ranges must be within the VPC's address space and must not overlap one another.

## Subnets

A subnet is an IP range in a single Availability Zone. Resources launched into a subnet use its route-table association and network ACL. A subnet is not inherently public or private; its routes and address-assignment behavior determine the connectivity it provides.

## Route tables

A route table contains destination-to-target routes used by resources in associated subnets. Every subnet has an explicit or main route-table association. A route such as `0.0.0.0/0` determines the default IPv4 path; the target may be an Internet Gateway, NAT Gateway, virtual private gateway, transit gateway, or another supported target. More specific routes take precedence over less-specific routes.

## Internet Gateway

An Internet Gateway (IGW) attaches to a VPC and enables internet routing for resources with suitable routes and addressing. A public subnet commonly has a default route to an IGW. For an instance to communicate directly with the public internet, it also needs a public IPv4 address or IPv6 address and permissive-enough Security Group, network ACL, and host firewall rules.

## NAT Gateway

A NAT Gateway lets resources in a private subnet initiate connections to external IPv4 destinations without accepting unsolicited inbound internet connections. A public NAT Gateway is placed in a public subnet and uses an Elastic IP; private subnet route tables direct internet-bound IPv4 traffic to it. For resilience, production designs commonly use a NAT Gateway per Availability Zone and route each private subnet to its local NAT. NAT Gateways incur hourly and data-processing charges; VPC endpoints may be more appropriate for traffic to supported AWS services.

## Security Groups

Security Groups are stateful allow-list firewalls associated with network interfaces. They control inbound and outbound traffic and automatically allow response traffic for permitted connections. Use the smallest required set of protocols, ports, and peer sources. Security Group references can be used for communication between supported resources without hard-coding changing IP addresses.

## Network ACLs

Network Access Control Lists (network ACLs) are stateless subnet-level filters. They support ordered allow and deny rules and apply to inbound and outbound traffic, so return traffic must be allowed explicitly. Network ACLs are an additional layer; Security Groups are typically the primary workload-level firewall.

## Public vs. private subnet

- A **public subnet** has a route to an Internet Gateway. Resources still need suitable IP addressing and firewall rules to be reachable from the internet.
- A **private subnet** has no direct route to an Internet Gateway for general inbound/outbound internet access. It may route outbound IPv4 traffic through a NAT Gateway, or access services through VPC endpoints.

Terminology describes route design, not a security guarantee. A public subnet is not automatically reachable, and a private subnet can still have access through peering, transit gateways, VPN, Direct Connect, or other paths.

## Common design pattern

Use public subnets for internet-facing load balancers and NAT Gateways, and private subnets for application and database tiers. Place resources across multiple Availability Zones, constrain Security Groups to specific tiers, and use VPC endpoints for private access to supported AWS services. Avoid placing a database in a public subnet unless there is a compelling, tightly controlled requirement.

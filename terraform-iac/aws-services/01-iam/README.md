# AWS IAM: Identity and Access Management

## What is IAM?

AWS Identity and Access Management (IAM) controls who can authenticate to AWS and what authenticated identities are allowed to do. IAM is a global service: identities and policies are not created separately per AWS Region. Authorization is evaluated for each request using the applicable identity-based and resource-based policies, permission boundaries, session policies, service control policies (SCPs), resource control policies (RCPs) where supported, and other applicable controls.

## IAM identities

### Users

An IAM user represents a long-term identity in one AWS account. Users can have console credentials and/or access keys, but long-lived credentials require careful lifecycle management. For people, AWS recommends federation through an identity provider and temporary role sessions instead of creating long-lived IAM users and keys where possible.

### Groups

An IAM group is a collection of IAM users to which identity-based policies can be attached. Groups simplify permission administration for user populations, but groups cannot contain other groups and are not identities that can sign in or assume roles.

### Roles

An IAM role is an identity with permissions that can be assumed to obtain temporary credentials. A role has:

- A **trust policy** that defines which principals may assume it and under what conditions.
- **Permissions policies** that specify the actions and resources permitted during the role session.

Roles are commonly used by AWS services, federated human users, applications running outside AWS, and cross-account access. Prefer short-lived role credentials to embedded access keys.

## Policies, permissions, and evaluation

Policies are JSON documents containing statements that define `Effect` (`Allow` or `Deny`), `Action` or `NotAction`, `Resource` or `NotResource`, and optional `Condition` clauses.

Common policy types:

- **Identity-based policies** attach to users, groups, or roles and grant or deny access.
- **Resource-based policies** attach to supported resources, such as S3 buckets, and identify principals and allowed actions.
- **Trust policies** are resource-based policies on roles that control assumption.
- **Permissions boundaries** set the maximum permissions an identity-based policy can grant to a user or role.
- **Session policies** can further restrict a role session.
- **Organizations SCPs/RCPs** set permission guardrails for accounts or resources in an AWS Organization; an SCP does not itself grant permissions.

An explicit `Deny` overrides an `Allow`. A request needs an applicable allow and must not be blocked by an applicable explicit deny or higher-level guardrail. Policy evaluation depends on the principal, resource, action, conditions, and service-specific authorization behavior.

## Least privilege

Least privilege means granting only the actions, resources, and conditions needed for a defined task—and removing permissions when they are no longer needed. Prefer resource ARNs and conditions over `"Resource": "*"`, and separate read, write, and administrative roles where practical.

## IAM best practices

- Require MFA for human access, especially privileged access; prefer phishing-resistant MFA where supported.
- Use federation and IAM Identity Center for workforce access; use temporary credentials and roles.
- Do not share credentials or embed access keys in code, images, shell history, or source control.
- Avoid root-user access for everyday work; protect root with MFA and do not create root access keys.
- Grant least privilege, review permissions regularly, and remove unused identities, policies, and keys.
- Use IAM Access Analyzer and service last-accessed information to help refine permissions.
- Add conditions where useful, such as required MFA, source network, organization, or encryption context.
- Separate duties and use permission boundaries and Organizations guardrails where appropriate.
- Enable CloudTrail and monitor sensitive IAM changes and unusual authentication activity.
- Rotate or revoke exposed credentials promptly; prefer temporary session credentials instead of routine manual key rotation.

## Common use cases

- Giving an EC2 instance or Lambda function permission to access a specific S3 bucket through an execution role.
- Allowing a federated employee to access a limited set of AWS accounts and services.
- Granting a CI/CD workflow temporary permission to publish an image or deploy infrastructure.
- Allowing cross-account access through a narrowly scoped role and trusted account.
- Enforcing organization-wide restrictions with Organizations policies.

## Example: application role permissions

An application that only reads objects in one bucket should receive the minimum required `s3:GetObject` access to that bucket's object ARN, with separate permissions for listing the bucket only if needed. Do not attach broad `AdministratorAccess` just to resolve an access-denied error; inspect CloudTrail and policy evaluation first.

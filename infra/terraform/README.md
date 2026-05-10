# Terraform Components

This directory contains a single Terraform root module for the mellow-wombat AWS storage components in us-west-2.

## What it creates

- An S3 general purpose bucket named `mellow-wombat.braingang.net`
- Default S3 encryption with SSE-S3 (`AES256`)
- Public access blocks for the bucket
- Lifecycle management that transitions objects to `STANDARD_IA` after 30 days
- Placeholder prefix objects for:
  - `wombat/`
  - `wombat/admin/`
  - `heeler2/`
  - `heeler2/fresh/`
  - `heeler2/archive/`
- IAM customer-managed policies:
  - `wombat-reader`
  - `wombat-writer`
  - `heeler2-writer`
  - `heeler2-archiver`

## Files

- `versions.tf`: Terraform version, AWS provider version, and the S3 backend block
- `providers.tf`: AWS provider configuration using region `us-west-2` and profile `terraform_braingang` by default
- `variables.tf`: provider and region inputs
- `locals.tf`: bucket name and S3 prefix placeholders
- `s3.tf`: bucket, encryption, public access block, lifecycle, and placeholder objects
- `iam.tf`: customer-managed IAM policies for the S3 access patterns
- `outputs.tf`: bucket name and policy ARN outputs
- `terraform.tfvars.example`: optional example provider override

## Backend configuration

The Terraform state bucket already exists, and the state key for this project is `wombat`. The backend block in `versions.tf` is intentionally partial so the bucket name can be supplied at init time.

Initialize with explicit backend settings:

```bash
terraform -chdir=infra/terraform init \
  -backend-config="bucket=<existing-state-bucket>" \
  -backend-config="key=wombat" \
  -backend-config="region=us-west-2" \
  -backend-config="profile=terraform_braingang"
```

No DynamoDB lock table is configured.

## Usage

1. Optionally copy `terraform.tfvars.example` to `terraform.tfvars` only if you need to override the default AWS profile.
2. Initialize Terraform with the existing S3 state bucket.
3. Review the plan.
4. Apply the configuration.
5. Attach the created IAM policies to the existing IAM users, groups, or permission sets outside Terraform.

Example:

```bash
terraform -chdir=infra/terraform plan
terraform -chdir=infra/terraform apply
```

If you do need a local profile override, create `terraform.tfvars` from the example first:

```bash
cp infra/terraform/terraform.tfvars.example infra/terraform/terraform.tfvars
```

Do not commit `terraform.tfvars`, backend config files, or other environment-specific credentials or identifiers into this public repository.

## Access model

The policies are designed around S3 prefixes:

- `wombat-reader`: list and read only under `wombat/admin/`
- `wombat-writer`: list, read, write, and delete only under `wombat/admin/`
- `heeler2-writer`: list, read, write, and delete only under `heeler2/fresh/`
- `heeler2-archiver`: list under `heeler2/fresh/` and `heeler2/archive/`, read from `heeler2/fresh/`, write to `heeler2/archive/`, and delete from `heeler2/fresh/`

These are attachable IAM policies, not assume-role identities. Existing IAM users cannot have a role directly attached in the console; they can have policies attached directly or via groups. This module now creates the policies so you can attach them manually to the existing identities you manage elsewhere.

## Current plan shape

With the current configuration, `terraform plan` shows `13 to add, 0 to change, 0 to destroy`.

The planned resources are:

- 1 S3 bucket
- 1 S3 public access block
- 1 S3 default encryption configuration
- 1 S3 lifecycle configuration
- 5 zero-byte S3 prefix placeholder objects
- 4 customer-managed IAM policies

## Gaps and remedies

1. `STANDARD_IA` cannot be used earlier than 30 days after object creation. This configuration uses 30 days because that is the earliest transition S3 allows for this storage class.
2. S3 prefixes are not real directories. The configuration creates zero-byte placeholder objects ending in `/` so the paths appear immediately in the console.
3. The module does not attach policies to users because those identities are managed outside Terraform. Remedy: attach the generated policies manually in the AWS console, via groups, or via your external IAM management process.
4. The backend state bucket name was not provided. Remedy: supply it during `terraform init` with `-backend-config`; this module expects the state object key to be `wombat`.
5. AWS now applies default transition-size behavior for smaller objects. Large files will transition as expected; very small objects may remain in `STANDARD` depending on current S3 lifecycle defaults.
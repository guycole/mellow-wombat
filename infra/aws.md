# AWS

## User Management
Each crate has a dedicated AWS user with IAM roles/policies that match the shelves.  If a crate is lost, it will be a simple matter to deactivate the user.

## S3
Each application has a dedicated S3 bucket with write only access

| Application | Bucket                       | Policy                    |
| ----------- | ---------------------------- | ------------------------- |
| heeler      | mellow-heeler.braingang.net  | mellow-heeler-write-only  |
| hyena       | mellow-hyena.braingang.net   | mellow-hyena-write-only   |
| koala       | mellow-koala.braingang.net   | mellow-koala-write-only   |
| manatee     | mellow-manatee.braingang.net | mellow-manatee-write-only |

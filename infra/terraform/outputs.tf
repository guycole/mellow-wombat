output "bucket_name" {
  description = "Name of the application bucket."
  value       = aws_s3_bucket.mellow_wombat.bucket
}

output "policy_arns" {
  description = "ARNs for the IAM policies created by this stack."
  value = {
    wombat_reader    = aws_iam_policy.wombat_reader.arn
    wombat_writer    = aws_iam_policy.wombat_writer.arn
    heeler2_writer   = aws_iam_policy.heeler2_writer.arn
    heeler2_archiver = aws_iam_policy.heeler2_archiver.arn
  }
}
resource "aws_s3_bucket" "mellow_wombat" {
  bucket = local.bucket_name
}

resource "aws_s3_bucket_public_access_block" "mellow_wombat" {
  bucket = aws_s3_bucket.mellow_wombat.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "mellow_wombat" {
  bucket = aws_s3_bucket.mellow_wombat.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "mellow_wombat" {
  bucket = aws_s3_bucket.mellow_wombat.id

  rule {
    id     = "transition-to-standard-ia"
    status = "Enabled"

    filter {}

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }
  }
}

resource "aws_s3_object" "prefix_placeholders" {
  for_each = local.placeholder_prefixes

  bucket  = aws_s3_bucket.mellow_wombat.id
  key     = each.value
  content = ""
}
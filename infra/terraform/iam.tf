data "aws_iam_policy_document" "wombat_reader_access" {
  statement {
    sid    = "ListWombatAdminPrefix"
    effect = "Allow"
    actions = [
      "s3:GetBucketLocation",
      "s3:ListBucket",
    ]
    resources = [aws_s3_bucket.mellow_wombat.arn]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values   = ["wombat/admin", "wombat/admin/*"]
    }
  }

  statement {
    sid    = "ReadWombatAdminObjects"
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:GetObjectVersion",
    ]
    resources = ["${aws_s3_bucket.mellow_wombat.arn}/wombat/admin/*"]
  }
}

resource "aws_iam_policy" "wombat_reader" {
  name   = "wombat-reader"
  policy = data.aws_iam_policy_document.wombat_reader_access.json
}

data "aws_iam_policy_document" "wombat_writer_access" {
  statement {
    sid    = "ListWombatAdminPrefix"
    effect = "Allow"
    actions = [
      "s3:GetBucketLocation",
      "s3:ListBucket",
    ]
    resources = [aws_s3_bucket.mellow_wombat.arn]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values   = ["wombat/admin", "wombat/admin/*"]
    }
  }

  statement {
    sid    = "WriteWombatAdminObjects"
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:GetObjectVersion",
      "s3:PutObject",
      "s3:DeleteObject",
    ]
    resources = ["${aws_s3_bucket.mellow_wombat.arn}/wombat/admin/*"]
  }
}

resource "aws_iam_policy" "wombat_writer" {
  name   = "wombat-writer"
  policy = data.aws_iam_policy_document.wombat_writer_access.json
}

data "aws_iam_policy_document" "heeler2_writer_access" {
  statement {
    sid    = "ListHeeler2FreshPrefix"
    effect = "Allow"
    actions = [
      "s3:GetBucketLocation",
      "s3:ListBucket",
    ]
    resources = [aws_s3_bucket.mellow_wombat.arn]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values   = ["heeler2/fresh", "heeler2/fresh/*"]
    }
  }

  statement {
    sid    = "WriteHeeler2FreshObjects"
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:GetObjectVersion",
      "s3:PutObject",
      "s3:DeleteObject",
    ]
    resources = ["${aws_s3_bucket.mellow_wombat.arn}/heeler2/fresh/*"]
  }
}

resource "aws_iam_policy" "heeler2_writer" {
  name   = "heeler2-writer"
  policy = data.aws_iam_policy_document.heeler2_writer_access.json
}

data "aws_iam_policy_document" "heeler2_archiver_access" {
  statement {
    sid    = "ListHeeler2Prefixes"
    effect = "Allow"
    actions = [
      "s3:GetBucketLocation",
      "s3:ListBucket",
    ]
    resources = [aws_s3_bucket.mellow_wombat.arn]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values = [
        "heeler2/fresh",
        "heeler2/fresh/*",
        "heeler2/archive",
        "heeler2/archive/*",
      ]
    }
  }

  statement {
    sid    = "ReadHeeler2FreshObjects"
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:GetObjectVersion",
    ]
    resources = ["${aws_s3_bucket.mellow_wombat.arn}/heeler2/fresh/*"]
  }

  statement {
    sid    = "ArchiveHeeler2Objects"
    effect = "Allow"
    actions = [
      "s3:PutObject",
      "s3:DeleteObject",
    ]
    resources = [
      "${aws_s3_bucket.mellow_wombat.arn}/heeler2/fresh/*",
      "${aws_s3_bucket.mellow_wombat.arn}/heeler2/archive/*",
    ]
  }
}

resource "aws_iam_policy" "heeler2_archiver" {
  name   = "heeler2-archiver"
  policy = data.aws_iam_policy_document.heeler2_archiver_access.json
}
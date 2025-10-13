# IAM role for GitHub Actions OIDC
# This allows GitHub Actions to authenticate with AWS without long-lived credentials

data "aws_caller_identity" "current" {}

# OIDC Provider for GitHub Actions
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = [
    "sts.amazonaws.com"
  ]

  thumbprint_list = [
    "6938fd4d98bab03faadb97b34396831e3780aea1",
    "1c58a3a8518e8759bf075b76b750d4f2df264fcd"
  ]

  tags = merge(
    var.tags,
    {
      Name = "GitHub Actions OIDC Provider"
    }
  )
}

# IAM Role for GitHub Actions
resource "aws_iam_role" "github_actions" {
  name               = "GitHubActionsDeployRole"
  description        = "Role for GitHub Actions to deploy to S3 and invalidate CloudFront"
  assume_role_policy = data.aws_iam_policy_document.github_actions_assume_role.json

  tags = merge(
    var.tags,
    {
      Name = "GitHub Actions Deploy Role"
    }
  )
}

# Trust policy for GitHub OIDC
data "aws_iam_policy_document" "github_actions_assume_role" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRoleWithWebIdentity"]

    principals {
      type        = "Federated"
      identifiers = [aws_iam_openid_connect_provider.github.arn]
    }

    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }

    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values   = ["repo:PythonMexico/pythonCDMX:*"]
    }
  }
}

# Policy for S3 access (production and staging)
data "aws_iam_policy_document" "github_actions_s3" {
  statement {
    sid    = "AllowS3AccessProduction"
    effect = "Allow"

    actions = [
      "s3:PutObject",
      "s3:PutObjectAcl",
      "s3:GetObject",
      "s3:DeleteObject",
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.website.arn,
      "${aws_s3_bucket.website.arn}/*"
    ]
  }

  statement {
    sid    = "AllowS3AccessStaging"
    effect = "Allow"

    actions = [
      "s3:PutObject",
      "s3:PutObjectAcl",
      "s3:GetObject",
      "s3:DeleteObject",
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.website_staging.arn,
      "${aws_s3_bucket.website_staging.arn}/*"
    ]
  }
}

# Policy for CloudFront invalidation (production and staging)
data "aws_iam_policy_document" "github_actions_cloudfront" {
  statement {
    sid    = "AllowCloudFrontInvalidation"
    effect = "Allow"

    actions = [
      "cloudfront:CreateInvalidation",
      "cloudfront:GetInvalidation",
      "cloudfront:ListInvalidations"
    ]

    resources = [
      aws_cloudfront_distribution.website.arn,
      aws_cloudfront_distribution.website_staging.arn
    ]
  }
}

# Attach S3 policy to role
resource "aws_iam_role_policy" "github_actions_s3" {
  name   = "S3AccessPolicy"
  role   = aws_iam_role.github_actions.id
  policy = data.aws_iam_policy_document.github_actions_s3.json
}

# Attach CloudFront policy to role
resource "aws_iam_role_policy" "github_actions_cloudfront" {
  name   = "CloudFrontAccessPolicy"
  role   = aws_iam_role.github_actions.id
  policy = data.aws_iam_policy_document.github_actions_cloudfront.json
}

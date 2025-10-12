# S3 bucket for staging website content
resource "aws_s3_bucket" "website_staging" {
  bucket = var.staging_bucket_name

  tags = merge(
    var.tags,
    {
      Name        = "PythonCDMX Website Staging"
      Environment = "staging"
    }
  )
}

# Enable versioning for staging bucket
resource "aws_s3_bucket_versioning" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Block public access at bucket level (CloudFront OAC will handle access)
resource "aws_s3_bucket_public_access_block" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Bucket policy to allow CloudFront access
resource "aws_s3_bucket_policy" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowCloudFrontServicePrincipal"
        Effect = "Allow"
        Principal = {
          Service = "cloudfront.amazonaws.com"
        }
        Action   = "s3:GetObject"
        Resource = "${aws_s3_bucket.website_staging.arn}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = aws_cloudfront_distribution.website_staging.arn
          }
        }
      }
    ]
  })

  depends_on = [aws_cloudfront_distribution.website_staging]
}

# Enable server-side encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Configure lifecycle rules - more aggressive cleanup for staging
resource "aws_s3_bucket_lifecycle_configuration" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  rule {
    id     = "delete-old-versions"
    status = "Enabled"

    noncurrent_version_expiration {
      noncurrent_days = 30 # Shorter retention for staging
    }
  }

  rule {
    id     = "delete-incomplete-uploads"
    status = "Enabled"

    abort_incomplete_multipart_upload {
      days_after_initiation = 3
    }
  }
}

# CORS configuration for website assets
resource "aws_s3_bucket_cors_configuration" "website_staging" {
  bucket = aws_s3_bucket.website_staging.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD"]
    allowed_origins = [
      "https://${var.staging_subdomain}"
    ]
    expose_headers  = ["ETag"]
    max_age_seconds = 3600
  }
}

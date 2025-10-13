# Origin Access Control for S3 Staging
resource "aws_cloudfront_origin_access_control" "website_staging" {
  name                              = "pythoncdmx-oac-staging"
  description                       = "OAC for PythonCDMX staging website"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# CloudFront distribution for staging
resource "aws_cloudfront_distribution" "website_staging" {
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  price_class         = "PriceClass_100" # Use only North America and Europe
  comment             = "PythonCDMX Community Website - Staging"

  aliases = [var.staging_subdomain]

  origin {
    domain_name              = aws_s3_bucket.website_staging.bucket_regional_domain_name
    origin_id                = "S3-${var.staging_bucket_name}"
    origin_access_control_id = aws_cloudfront_origin_access_control.website_staging.id
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${var.staging_bucket_name}"

    forwarded_values {
      query_string = false
      headers      = ["Origin", "Access-Control-Request-Method", "Access-Control-Request-Headers"]

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 300     # 5 minutes - shorter cache for staging
    max_ttl                = 3600    # 1 hour - shorter cache for staging
    compress               = true
  }

  # Cache behavior for static assets (CSS) - shorter cache for staging
  ordered_cache_behavior {
    path_pattern     = "/css/*"
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${var.staging_bucket_name}"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 1800    # 30 minutes
    max_ttl                = 7200    # 2 hours
    compress               = true
  }

  # Cache behavior for static assets (JS) - shorter cache for staging
  ordered_cache_behavior {
    path_pattern     = "/js/*"
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${var.staging_bucket_name}"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 1800    # 30 minutes
    max_ttl                = 7200    # 2 hours
    compress               = true
  }

  # Cache behavior for images - shorter cache for staging
  ordered_cache_behavior {
    path_pattern     = "/images/*"
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${var.staging_bucket_name}"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600    # 1 hour
    max_ttl                = 86400   # 24 hours
    compress               = true
  }

  # Custom error responses for SPA-like behavior
  custom_error_response {
    error_code         = 404
    response_code      = 404
    response_page_path = "/404.html"
  }

  custom_error_response {
    error_code         = 403
    response_code      = 404
    response_page_path = "/404.html"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate.website_staging.arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }

  tags = merge(
    var.tags,
    {
      Name        = "PythonCDMX Website Distribution - Staging"
      Environment = "staging"
    }
  )

  depends_on = [aws_acm_certificate_validation.website_staging]
}

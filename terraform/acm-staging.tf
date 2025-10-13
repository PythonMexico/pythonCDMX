# ACM certificate for CloudFront staging (must be in us-east-1)
resource "aws_acm_certificate" "website_staging" {
  provider = aws.us_east_1

  domain_name       = var.staging_subdomain
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }

  tags = merge(
    var.tags,
    {
      Name        = "PythonCDMX Website Certificate - Staging"
      Environment = "staging"
    }
  )
}

# Certificate validation for staging
resource "aws_acm_certificate_validation" "website_staging" {
  provider = aws.us_east_1

  certificate_arn         = aws_acm_certificate.website_staging.arn
  validation_record_fqdns = [for record in aws_route53_record.certificate_validation_staging : record.fqdn]

  timeouts {
    create = "45m"
  }
}

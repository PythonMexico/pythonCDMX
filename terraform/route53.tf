# Data source for existing hosted zone
data "aws_route53_zone" "main" {
  name         = var.domain_name
  private_zone = false
}

# ============================================================================
# PRODUCTION ENVIRONMENT - pythoncdmx.org
# ============================================================================

# A record for root domain (pythoncdmx.org) pointing to CloudFront
resource "aws_route53_record" "website_root" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = var.domain_name
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.website.domain_name
    zone_id                = aws_cloudfront_distribution.website.hosted_zone_id
    evaluate_target_health = false
  }
}

# AAAA record for IPv6 support (root domain)
resource "aws_route53_record" "website_root_ipv6" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = var.domain_name
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.website.domain_name
    zone_id                = aws_cloudfront_distribution.website.hosted_zone_id
    evaluate_target_health = false
  }
}

# A record for www subdomain pointing to CloudFront
resource "aws_route53_record" "website_www" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "www.${var.domain_name}"
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.website.domain_name
    zone_id                = aws_cloudfront_distribution.website.hosted_zone_id
    evaluate_target_health = false
  }
}

# AAAA record for IPv6 support (www subdomain)
resource "aws_route53_record" "website_www_ipv6" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "www.${var.domain_name}"
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.website.domain_name
    zone_id                = aws_cloudfront_distribution.website.hosted_zone_id
    evaluate_target_health = false
  }
}

# ============================================================================
# STAGING ENVIRONMENT - staging.pythoncdmx.org
# ============================================================================

# A record for staging subdomain pointing to CloudFront staging distribution
resource "aws_route53_record" "website_staging" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = var.staging_subdomain
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.website_staging.domain_name
    zone_id                = aws_cloudfront_distribution.website_staging.hosted_zone_id
    evaluate_target_health = false
  }
}

# AAAA record for IPv6 support (staging subdomain)
resource "aws_route53_record" "website_staging_ipv6" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = var.staging_subdomain
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.website_staging.domain_name
    zone_id                = aws_cloudfront_distribution.website_staging.hosted_zone_id
    evaluate_target_health = false
  }
}

# ============================================================================
# ACM CERTIFICATE VALIDATION RECORDS
# ============================================================================

# Validation records for production certificate
resource "aws_route53_record" "certificate_validation" {
  for_each = {
    for dvo in aws_acm_certificate.website.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.main.zone_id
}

# Validation records for staging certificate
resource "aws_route53_record" "certificate_validation_staging" {
  for_each = {
    for dvo in aws_acm_certificate.website_staging.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.main.zone_id
}

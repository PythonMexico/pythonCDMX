output "website_bucket_name" {
  description = "Name of the S3 bucket hosting the website"
  value       = aws_s3_bucket.website.id
}

output "website_bucket_arn" {
  description = "ARN of the S3 bucket hosting the website"
  value       = aws_s3_bucket.website.arn
}

output "cloudfront_distribution_id" {
  description = "ID of the CloudFront distribution"
  value       = aws_cloudfront_distribution.website.id
}

output "cloudfront_domain_name" {
  description = "Domain name of the CloudFront distribution"
  value       = aws_cloudfront_distribution.website.domain_name
}

output "certificate_arn" {
  description = "ARN of the ACM certificate"
  value       = aws_acm_certificate.website.arn
}

output "certificate_validation_records" {
  description = "DNS validation records for the certificate"
  value = [
    for dvo in aws_acm_certificate.website.domain_validation_options : {
      name   = dvo.resource_record_name
      type   = dvo.resource_record_type
      value  = dvo.resource_record_value
    }
  ]
}

output "website_url" {
  description = "URL of the website (production)"
  value       = "https://${var.domain_name}"
}

# ============================================================================
# STAGING ENVIRONMENT OUTPUTS
# ============================================================================

output "staging_bucket_name" {
  description = "Name of the S3 bucket hosting the staging website"
  value       = aws_s3_bucket.website_staging.id
}

output "staging_bucket_arn" {
  description = "ARN of the S3 bucket hosting the staging website"
  value       = aws_s3_bucket.website_staging.arn
}

output "staging_cloudfront_distribution_id" {
  description = "ID of the CloudFront distribution (staging)"
  value       = aws_cloudfront_distribution.website_staging.id
}

output "staging_cloudfront_domain_name" {
  description = "Domain name of the CloudFront distribution (staging)"
  value       = aws_cloudfront_distribution.website_staging.domain_name
}

output "staging_certificate_arn" {
  description = "ARN of the ACM certificate (staging)"
  value       = aws_acm_certificate.website_staging.arn
}

output "staging_website_url" {
  description = "URL of the staging website"
  value       = "https://${var.staging_subdomain}"
}

# ============================================================================
# ROUTE53 OUTPUTS
# ============================================================================

output "hosted_zone_id" {
  description = "ID of the Route53 hosted zone"
  value       = data.aws_route53_zone.main.zone_id
}

output "hosted_zone_name_servers" {
  description = "Name servers for the hosted zone"
  value       = data.aws_route53_zone.main.name_servers
}

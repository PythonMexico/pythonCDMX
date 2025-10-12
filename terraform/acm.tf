# ACM certificate for CloudFront (must be in us-east-1)
resource "aws_acm_certificate" "website" {
  provider = aws.us_east_1

  domain_name               = var.domain_name
  subject_alternative_names = var.alternative_domain_names
  validation_method         = "DNS"

  lifecycle {
    create_before_destroy = true
  }

  tags = merge(
    var.tags,
    {
      Name = "PythonCDMX Website Certificate"
    }
  )
}

# Certificate validation
resource "aws_acm_certificate_validation" "website" {
  provider = aws.us_east_1

  certificate_arn = aws_acm_certificate.website.arn

  timeouts {
    create = "45m"
  }
}

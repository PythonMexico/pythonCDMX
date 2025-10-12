variable "aws_region" {
  description = "AWS region for the infrastructure"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (production, staging)"
  type        = string
  default     = "production"
}

variable "domain_name" {
  description = "Primary domain name for the website"
  type        = string
  default     = "pythoncdmx.org"
}

variable "alternative_domain_names" {
  description = "Alternative domain names (e.g., www subdomain)"
  type        = list(string)
  default     = ["www.pythoncdmx.org"]
}

variable "staging_subdomain" {
  description = "Subdomain for staging environment"
  type        = string
  default     = "staging.pythoncdmx.org"
}

variable "bucket_name" {
  description = "S3 bucket name for website hosting (production)"
  type        = string
  default     = "pythoncdmx-website"
}

variable "staging_bucket_name" {
  description = "S3 bucket name for staging website"
  type        = string
  default     = "pythoncdmx-website-staging"
}

variable "terraform_state_bucket" {
  description = "S3 bucket name for Terraform state"
  type        = string
  default     = "pythoncdmx-terraform-state"
}

variable "terraform_locks_table" {
  description = "DynamoDB table for Terraform state locks"
  type        = string
  default     = "pythoncdmx-terraform-locks"
}

variable "tags" {
  description = "Additional tags for resources"
  type        = map(string)
  default     = {}
}

variable "project_id" {
  type        = string
  description = "Project ID"
}

variable "env_name" {
  type        = string
  description = "Project environment"
  default     = "live"
}

variable "aws_account_id" {
  type        = string
  description = "AWS Account ID"
}

variable "aws_region" {
  type        = string
  description = "Defines where your app should be deployed"
  default     = "eu-west-1"
}

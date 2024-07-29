terraform {
    backend "s3" {
      bucket = "<YOUR BUCKET NAME>"
      key    = "spark-dynamodb/terraform.tfstate"
      region = "eu-west-1"
    }
}

provider "aws" {
  region  = var.aws_region
}

module "dynamodb" {
  source = "./modules/dynamodb/"

  project_id     = var.project_id
  env_name       = var.env_name
  aws_account_id = var.aws_account_id
  aws_region     = var.aws_region
}

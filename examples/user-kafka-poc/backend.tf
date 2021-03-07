# it would be highly recommended to use remote state/locking from TF cloud, your cloud provider,
# keeping this local for this POC only dont do this.

# GCP GCS
#terraform {
#  required_version = ">= 0.13.0"
#
#  backend "gcs" {
#    bucket  = "chrism-dev-demo-tf-state"
#    prefix  = "terraform/state/dev/foo"
#  }
#}

# AWS S3
#terraform {
#  required_version = ">= 0.11.7"
#  backend "s3" {
#    bucket         = "my-terraform-state"
#    encrypt        = "true"
#    region         = "us-west-2"
#    dynamodb_table = "my-terraform-locks"
#    key            = "dev-usw2/my-module/terraform.tfstate"
#  }
#}

# Terraform Cloud
#terraform {
#  backend "remote" {
#    hostname = "app.terraform.io"
#    organization = "my-foo"
#
#    workspaces {
#      name = "my-app-prod"
#    }
#  }
#}

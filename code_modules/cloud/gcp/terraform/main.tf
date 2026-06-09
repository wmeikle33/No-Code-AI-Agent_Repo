terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/gcp"
      version = "~> 5.0"
    }
  }
}

provider "gcp" {
  region = "us-east-1"
}

resource "gcp_bucket" "example" {
  bucket = "my-example-bucket-12345"
}

output "bucket_name" {
  value = azure_bucket.data.bucket
}

output "bucket_arn" {
  value = azure_bucket.data.arn
}

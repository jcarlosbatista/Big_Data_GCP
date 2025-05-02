
# The 'Google Cloud Storage' library will be imported!
from google.cloud import storage

# Python's standad libraru comes included, and doesn't require installation.
import sys

# Authenticate Service Account based on credential files (key - Json)
key = sys.argv[1]
storage_client = storage.Client.from_service_account_json(key)

bucket_name = "tcb-gcp-carlos-batista-03"
bucket = storage_client.create_bucket(bucket_name)

# Lising GCP Cloud Storage Buckets
buckets = list(storage_client.list_buckets())
print(*buckets, sep='\n')


import sys
import os
from google.cloud import storage

if len(sys.argv) < 2:
    print("Uso: python list_storage.py <caminho_para_json>")
    sys.exit(1)

key = sys.argv[1]

if not os.path.exists(key):
    print(f"Arquivo não encontrado: {key}")
    sys.exit(1)

storage_client = storage.Client.from_service_account_json(key)

buckets = list(storage_client.list_buckets())

if not buckets:
    print("Nenhum bucket encontrado.")
else:
    print("Buckets encontrados:")
    for bucket in buckets:
        print(f"- {bucket.name}")
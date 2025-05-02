from google.cloud import storage
import sys

def delete_all_buckets(key_path):
    storage_client = storage.Client.from_service_account_json(key_path)

    buckets = list(storage_client.list_buckets())

    if not buckets:
        print("Nenhum bucket encontrado.")
        return

    for bucket in buckets:
        print(f"🔍 Processando bucket: {bucket.name}")

        # Esvazia o bucket
        blobs = list(bucket.list_blobs())
        for blob in blobs:
            print(f"🗑️  Deletando objeto: {blob.name}")
            blob.delete()

        # Deleta o bucket
        bucket.delete()
        print(f"✅ Bucket deletado: {bucket.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python delete_all_buckets.py <caminho_para_chave_json>")
        sys.exit(1)

    key_file = sys.argv[1]
    delete_all_buckets(key_file)
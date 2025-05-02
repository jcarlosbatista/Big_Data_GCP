import sys
from google.cloud import storage


def create_bucket(bucket_name, location):
    """Creates a new bucket in the specified region or multi-region."""
    
    storage_client = storage.Client()
    bucket = storage.Bucket(storage_client, name=bucket_name)
    bucket.location = location
    bucket.storage_class = "STANDARD"

    bucket = storage_client.create_bucket(bucket)

    location_type = 'Multi-Regional' if location.upper() in ['US', 'EU', 'ASIA'] else 'Regional'
    print(f"Bucket '{bucket.name}' criado na {location_type} '{bucket.location}' com storage class '{bucket.storage_class}'.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python create_storage.py <bucket-name> [location]")
        sys.exit(1)

    bucket_name = sys.argv[1]
    location = sys.argv[2] if len(sys.argv) > 2 else "us"

    create_bucket(bucket_name, location)

# Quando criamos os buckets com US - Ele cria com Multi-Region
# Porém quando e criado com a region especifica fica com Region

# Valor de location     Tipo          Significado
# "us-east1"            Regional      Virgi­nia, EUA
# "southamerica-east1"  Regional      Sao Paulo, Brasil
# "US"                  Multi-region  Multi-regional em todas as regioees dos EUA
# "EU"                  Multi-region  Multi-regional na Europa
# "ASIA"                Multi-region  Multi-regional na Asia

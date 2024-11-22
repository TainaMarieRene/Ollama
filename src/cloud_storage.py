# cloud_storage.py
from google.cloud import storage

def download_documents_from_cloud(bucket_name, prefix=""):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)
    
    documents = []
    for blob in blobs:
        content = blob.download_as_text()
        documents.append(content)
    
    return documents 

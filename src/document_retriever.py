import boto3
import os

def retrieve_documents_from_s3(bucket_name):
    # Initialisation de la connexion à AWS
    s3 = boto3.client('s3')

    # Liste des fichiers dans le bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    documents = []
    
    # Récupérer le contenu des fichiers
    for obj in response.get('Contents', []):
        file_obj = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
        document = file_obj['Body'].read().decode('utf-8')
        documents.append(document)
    
    return documents

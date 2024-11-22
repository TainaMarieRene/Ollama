# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os
from document_retriever import retrieve_documents_from_s3
from rag import create_rag_chain, generate_answer_with_rag, generate_answer_without_rag

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Charger les documents depuis le cloud (par exemple, AWS S3)
documents = retrieve_documents_from_s3('your-bucket-name')

# Créer la chaîne RAG avec une température de 0.5
rag_chain = create_rag_chain(documents, temperature=0.5)

# Définir une question pour le test
question = "Quel est l'impact de l'intelligence artificielle sur l'économie ?"

# Réponse sans RAG
response_without_rag = generate_answer_without_rag(question)

# Réponse avec RAG
response_with_rag = generate_answer_with_rag(question, rag_chain)

# Afficher les résultats
print("Réponse sans RAG : ", response_without_rag)
print("Réponse avec RAG : ", response_with_rag)

# Changer la température et tester à nouveau
rag_chain_02 = create_rag_chain(documents, temperature=0.2)
response_with_rag_02 = generate_answer_with_rag(question, rag_chain_02)
print("Réponse avec temperature=0.2 : ", response_with_rag_02)

rag_chain_1_0 = create_rag_chain(documents, temperature=1.0)
response_with_rag_1_0 = generate_answer_with_rag(question, rag_chain_1_0)
print("Réponse avec temperature=1.0 : ", response_with_rag_1_0)

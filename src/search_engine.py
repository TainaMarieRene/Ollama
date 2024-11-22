# search_engine.py
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Créer le moteur de recherche à partir des documents
def create_vector_store(documents): 
    embeddings = OpenAIEmbeddings()  # Utilisation d'OpenAIEmbeddings pour convertir en vecteurs
    doc_search = FAISS.from_texts(documents, embeddings)  # Indexation avec FAISS
    return doc_search

# Recherche des documents pertinents par similitude
def retrieve_relevant_documents(query, doc_search):
    """Retourne les documents pertinents en fonction de la requête"""
    # Effectue la recherche de similarité
    relevant_docs = doc_search.similarity_search(query)
    return relevant_docs


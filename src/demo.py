# Importation des bibliothèques nécessaires
from langchain.llms import OpenAI  # Assurez-vous que LangChain est installé
import os

# Chargez la clé API depuis la variable d'environnement
from dotenv import load_dotenv
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour créer le modèle OpenAI avec une température spécifique
def create_rag_model(temperature=0.7):
    llm = OpenAI(temperature=temperature)  # Créez un modèle OpenAI avec la température souhaitée
    return llm

# Fonction pour générer une réponse sans utiliser RAG
def generate_answer_without_rag(query):
    """Génère une réponse sans utiliser RAG"""
    llm = OpenAI(temperature=0.7)  # Créez un modèle OpenAI
    response = llm(query)  # Génère une réponse basée sur la requête
    return response 

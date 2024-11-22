import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Accéder à la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Exemple d'appel à l'API OpenAI
response = openai.Completion.create(
    model="text-davinci-003",  # Modèle OpenAI
    prompt="Quel est le sens de la vie ?",  # Prompt pour l'API
    max_tokens=100  # Nombre maximum de tokens
)

# Afficher la réponse
print(response.choices[0].text.strip())
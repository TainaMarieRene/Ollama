# -*- coding: utf-8 -*-
import openai

# Effectuer une simple requête pour tester l'intégration avec l'API OpenAI
response = openai.Completion.create(
    model="text-davinci-003", 
    prompt="Quel est le sens de la vie ?", 
    max_tokens=100  # Limiter le nombre de tokens
)

# Afficher la réponse de l'API
print(response.choices[0].text.strip())

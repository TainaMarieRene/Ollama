
Dans ce petit projet, il s'agit d'implémenter un chatbot utilisant la technique RAG (Retrieve and Generate). Il répond aux questions en générant des réponses grâce à OpenAI et en combinant celles-ci avec des documents stockés dans le cloud (par exemple, AWS S3).

Python 3.11+ installé sur votre machine.
Clé API OpenAI : Inscrivez-vous sur OpenAI pour obtenir une clé.

Structure

/Ollama
├── .env                    - Clés API
├── requirements.txt        -  Dépendances
├── src/                    - Code source
│   ├── main.py             - Point d'entrée
│   ├── rag.py              - Logique RAG
│   ├── document_retriever.py -  Récupération de documents (S3)
└── README.md                - Instructions du projet


Lancer le projet : 
python src/main.py

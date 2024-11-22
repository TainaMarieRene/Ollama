from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
import faiss

def create_rag_chain(documents, temperature=0.7):
    # Créer un index FAISS avec les embeddings OpenAI
    embeddings = OpenAIEmbeddings()
    faiss_index = FAISS.from_texts(documents, embeddings)

    # Créer le modèle OpenAI avec la température spécifiée
    llm = OpenAI(temperature=temperature)
    
    # Créer une chaîne de récupération augmentée (RAG)
    rag_chain = ConversationalRetrievalChain.from_llm_and_retriever(
        llm, faiss_index.as_retriever()
    )
    
    return rag_chain

def generate_answer_with_rag(question, rag_chain):
    return rag_chain.run(question)

def generate_answer_without_rag(question):
    llm = OpenAI(temperature=0.7)
    return llm.predict(question)

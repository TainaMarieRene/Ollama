# temperature_tuning.py
from rag_model import create_rag_model, generate_answer_with_rag

def test_temperature(query, documents):
    for temp in [0.0, 0.5, 1.0]:
        print(f"Température = {temp}")
        rag_model = create_rag_model(temperature=temp)
        answer = generate_answer_with_rag(query, documents, rag_model)
        print(answer)

"""
Full RAG pipeline: Retriever + Generator with prompt template.
"""
from .retriever import Retriever
from .generator import Generator

class RAGPipeline:
    def init(self, retriever=None, generator=None):
        self.retriever = retriever or Retriever()
        self.generator = generator or Generator()

    def build_prompt(self, question, retrieved_chunks):
        context = ""
        for i, chunk in enumerate(retrieved_chunks, 1):
            context += f"\n[Excerpt {i} | Product: {chunk['product']}]\n{chunk['chunk_text']}\n"
        prompt = f"""You are a financial analyst assistant for CreditTrust.
Use ONLY the following complaint excerpts to answer the question.
If the excerpts do not contain enough information, say exactly: "I don't have enough information to answer that."
Do not add any information not present in the excerpts.

Retrieved excerpts:
{context}

Question: {question}

Answer:"""
        return prompt

    def query(self, question, top_k=5):
        retrieved = self.retriever.retrieve(question, top_k)
        prompt = self.build_prompt(question, retrieved)
        answer = self.generator.generate(prompt)
        return {
            'question': question,
            'answer': answer,
            'sources': retrieved
        }

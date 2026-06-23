"""
Generator module – LLM via Hugging Face Inference API.
"""
import os
from huggingface_hub import InferenceClient

class Generator:
    def init(self, model="Qwen/Qwen2.5-7B-Instruct", token=None):
        if token is None:
            token = os.getenv("HF_TOKEN")
        self.client = InferenceClient(model=model, token=token)

    def generate(self, prompt, max_new_tokens=300):
        response = self.client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_new_tokens,
        )
        return response.choices[0].message.content.strip()
      

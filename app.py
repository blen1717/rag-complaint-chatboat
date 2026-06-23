
import gradio as gr
from rag_pipeline import rag_pipeline  # adapt if needed

def respond(message, history):
    result = rag_pipeline(message)
    sources_text = ""
    for i, s in enumerate(result['sources'], 1):
        sources_text += f"\nSource {i} (Product: {s['product']}, Score: {s['score']:.3f}):\n"
        sources_text += s['chunk_text'][:300] + "...\n"
    return result['answer'] + "\n\n---\n\nSources:" + sources_text

demo = gr.ChatInterface(fn=respond, title="CreditTrust Complaint Assistant")
demo.launch(share=True)

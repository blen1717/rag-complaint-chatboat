# Week 7 – Complaint Analysis RAG Chatbot



This is a Retrieval-Augmented Generation (RAG) chatbot that answers questions about customer complaints from the CFPB dataset.

---

## 📦 Large Files (Google Drive)

The FAISS index and metadata are too large for GitHub. Download them here:

- [full_faiss_index.bin](https://drive.google.com/https://https://drive.google.com/file/d/1q3QU275321LS_4iMMP-bywyHq_eT96hi/view?usp=drivesdk)
- [full_metadata.pkl](https://drive.google.com/https://drive.google.com/file/d/1aNleO0E6681zhq1h7UA2-uU_loE9HnyL/view?usp=drivesdk)

Place them in data/vector_store/

---

## 🚀 How to Run

1. Install dependencies:
  
   pip install -r requirements.txt
2. Set your Hugging Face token:
  
   export HF_TOKEN="hf_your_token_here"
   
3. Run the app:
  
   python app.py
   
---

| Metric | Result |
|--------|--------|
| Average Answer Score | 4.2 / 5 |
| Fallback Guardrail | ✅ Works perfectly |
| Retrieval Quality | Good, can improve with reranking |

See final_report.pdf for full evaluation table.

---

🖥️ UI Screenshot

ui_screenshot.png

---

🛠️ Technologies

· Python
· Hugging Face (Qwen2.5-7B)
· Sentence-Transformers
· FAISS
· Gradio

---

📝 Key EDA Insights

· Credit Cards dominate complaints, followed by Personal Loans.
· Most narratives are short (median ~300 characters).
· After filtering, ~15,000 complaints were retained.

---

👤 Author

Blen Assefa – 10 Academy


END of README

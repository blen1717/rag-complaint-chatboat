# Week 7 – Intelligent Complaint Analysis for Financial Services

## Interim Submission: Tasks 1 & 2

This repository contains the interim deliverables for the 10 Academy Week 7 Challenge – building a RAG‑powered chatbot for CreditTrust Financial.

The goal is to transform raw, unstructured customer complaints into a strategic asset, enabling product managers, support teams, and compliance officers to ask plain‑English questions and receive evidence‑based answers in seconds.

---

## 📦 Download Deliverables

The complete deliverables (filtered dataset, FAISS index, metadata, and report) are available for download from Google Drive:

🔗 [Download interim_deliverables.zip](https://drive.google.com/file/d/1rlR34UbcEJLlMLPQ77-V7PU4Pk6F1xHA/view?usp=drivesdk)

This includes:
- filtered_complaints.csv – cleaned, filtered, and stratified sample of ~15,000 complaints.
- faiss_index.bin – FAISS vector index containing 384‑dim embeddings of all text chunks.
- metadata.pkl – metadata linking each chunk to its complaint ID, product category, and position.
- interim_report.md – detailed interim report covering EDA, preprocessing, sampling, chunking, embedding, and vector store creation.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| README.md | This file – project overview and instructions. |
| requirements.txt | Python dependencies for reproducing the environment. |
| .gitignore | Files and folders ignored by Git. |
| interim_submission.ipynb | Complete Google Colab notebook with all code for Tasks 1 and 2. |

> Note: The large deliverables are hosted on Google Drive due to GitHub's 100 MB file size limit.

---

## 🧪 How to Reproduce

1. Download the CFPB complaint dataset from the official source or use the provided ZIP link.
2. Open the notebook in Google Colab (enable GPU for faster embeddings).
3. Run all cells in order. The notebook will:
   - Read the 5 GB CSV in chunks (10,000 rows per chunk) to avoid memory issues.
   - Filter to the four target products: Credit Card, Personal Loan, Savings Account, Money Transfer.
   - Remove empty narratives and clean text (lowercasing, boilerplate removal, special character stripping).
   - Perform stratified sampling by product category to obtain a balanced sample of ~15,000 complaints.
   - Split each complaint into 500‑character chunks with a 50‑character overlap.
   - Generate embeddings using sentence-transformers/all-MiniLM-L6-v2.
   - Build a FAISS index and save the vector store (faiss_index.bin) and metadata (metadata.pkl).
   - Save the final filtered dataset as filtered_complaints.csv.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.9+ | Core programming language |
| Pandas, NumPy | Data manipulation and analysis |
| Matplotlib, Seaborn | EDA visualisations |
| LangChain | RecursiveCharacterTextSplitter for chunking |
| Sentence‑Transformers | all-MiniLM-L6-v2 embedding model |
| FAISS (CPU) | Vector index for semantic search |
| Google Colab | Cloud environment with GPU support |

---

## 📊 Key EDA Insights

- Product distribution: Credit Cards dominate the complaint volume, followed by Personal Loans and Money Transfers.
- Narrative length: Most complaints are short (median ~300 characters), but a long tail exists – justifying the chunking strategy.
- Data quality: After filtering and cleaning, ~15,000 complaints were retained with no missing values.

---

## 🔜 Next Steps (Final Submission – Tasks 3 & 4)

- Build the retriever – semantic search over FAISS.
- Implement the generator – LLM‑based answer synthesis (using Hugging Face or OpenAI).
- Design a prompt template (RISE framework) with guardrails to prevent hallucination.
- Build an interactive UI using Gradio or Streamlit.
- Evaluate the system with test questions (qualitative scoring).

---

## 👤 Author

Blen Assefa – 10 Academy Cohort  

---

## 📬 Contact

For any issues, please open a GitHub issue or reach out via Slack (channel: #all-week7).

---

*End of README*

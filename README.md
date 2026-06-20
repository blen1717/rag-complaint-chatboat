# Week 7 – Intelligent Complaint Analysis for Financial Services

## Interim Submission: Tasks 1 & 2

This repository contains the interim deliverables for the 10 Academy Week 7 Challenge – building a RAG‑powered chatbot for CreditTrust Financial.

### Deliverables
- **filtered_complaints.csv** – cleaned, filtered, and stratified sample of ~15,000 complaints.
- **faiss_index.bin** – FAISS vector index of chunk embeddings.
- **metadata.pkl** – chunk metadata (complaint ID, product, text).
- **interim_report.pdf** (or .md) – EDA findings, sampling, chunking, and embedColab notebookColab notebook** – complete code for Tasks 1 and 2.

### How to Reproduce
1. Download the CFPB complaint dataset (or use the provided ZIP).
2. Run the notebook in Google Colab (with GPU enabled).
3. The notebook will:
   - Read the 5 GB CSV in chunks,
   - Filter to the four target products,
   - Perform stratified sampling,
   - Clean text,
   - Chunk into 500‑character pieces (50 overlap),
   - Generate embeddings with all-MiniLM-L6-v2,
   - Build a FAISS index,
   - Save the final outputs.

### File Structure

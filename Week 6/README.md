# Week 6 — NLP Fundamentals: Tokenization, Text Chunking and Retrieval

**Student:** Ahsen  
**Roll No.:** 204  
**Course:** CAI601400 — Artificial Intelligence Lab

This folder contains a beginner-friendly Week 6 implementation using synthetic campus documents.

## Run
From this folder, install the dependencies and run:
```bash
pip install -r requirements.txt
python task1_tokens.py
python task2_chunks.py
python task3_retrieval.py
```

## Contents
- `task1_tokens.py`: whitespace and Unicode-aware word-like tokenization.
- `task2_chunks.py`: 40-word fixed windows with overlap 0 and 10, plus sentence-aware chunks; offsets and IDs are retained.
- `task3_retrieval.py`: TF-IDF retrieval, top-three rankings, Hit@3, MRR@3 and CSV output.
- `data/corpus.json`: five synthetic campus documents.
- `data/queries.json`: eight answerable queries (four dev, four held-out test) and two unanswerable queries.
- `outputs/`: generated chunk and retrieval outputs after running the scripts.

## Limitation
This version implements the TF-IDF retrieval path. It does **not** claim to have completed the sentence-transformer comparison. The manual's MiniLM embedding experiment requires installing `sentence-transformers` and downloading model weights. No embedding scores are invented. The corpus is synthetic and must not be treated as official university policy.
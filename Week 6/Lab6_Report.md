# AI Lab — Week 6 Report
## NLP Fundamentals: Tokenization, Text Chunking and Retrieval

**Student:** Ahsen  
**Roll No.:** 204  
**Course:** CAI601400 — Artificial Intelligence Lab

### Aim
Explore tokenization, source-preserving text chunking, and retrieval of relevant passages from a small synthetic corpus.

### Task 1 — Tokenization
Whitespace splitting separates text at spaces and leaves punctuation attached to tokens. A Unicode-aware word-like regular expression separates much punctuation and retains common apostrophe contractions. The examples include punctuation, contractions, an email address, a course identifier, empty text, and Urdu text. Regex tokenization is a simple demonstration, not a complete multilingual tokenizer. Normalization may damage meaningful structures such as email addresses and identifiers.

### Task 2 — Chunking
The code implements 40-word windows with overlap 0 and overlap 10, plus sentence-aware chunks with a 40-word target. Each chunk stores its source document ID, chunk ID, original character offsets, text, and word count. Overlap can preserve boundary-spanning facts but repeats text and increases chunk count. Sentence-aware splitting tries to preserve sentence boundaries but the simple punctuation splitter may mishandle abbreviations. Invalid overlap and non-positive chunk sizes are rejected.

### Task 3 — Retrieval
Five synthetic documents and ten questions are supplied: four development questions, four held-out test questions, and two unanswerable questions. TF-IDF with unigram/bigram features and cosine similarity ranks the top three chunks. The script writes retrieval evidence and computes Hit@3 and MRR@3 for answerable questions. Unanswerable questions still receive nearest passages, so a similarity score is not proof that an answer exists.

### Limitations
This uploaded implementation demonstrates the TF-IDF path only. It does not claim to have run the sentence-transformer MiniLM comparison described in the manual. No embedding metrics are fabricated. The corpus is synthetic and must not be treated as official university policy. Run the scripts locally to generate the CSV and metrics files before reporting exact measurements.

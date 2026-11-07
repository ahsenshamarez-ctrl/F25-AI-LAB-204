import re
samples = [
 "Hello, world! NLP is useful.",
 "I can't access my account; please help.",
 "student.name@example.edu",
 "CS4944_lab-6: tokenization & embeddings",
 "",
 "یہ اردو زبان کا ایک مختصر نمونہ ہے۔"
]
def whitespace_tokens(text):
    return text.split()
def word_like_tokens(text):
    return re.findall(r"[^W_]+(?:['’][^W_]+)?", text, flags=re.UNICODE)
if __name__ == "__main__":
    for i, s in enumerate(samples, 1):
        print(f"\n{i}. {s!r}")
        print("Whitespace:", whitespace_tokens(s))
        print("Word-like:", word_like_tokens(s))
    print("\nReasoning: whitespace splitting is simple but keeps punctuation attached.")
    print("The word-like pattern separates much punctuation and retains common contractions.")
    print("Normalization can damage identifiers, email addresses, names and code.")
    print("The Urdu sample tests Unicode handling; this is not a full Urdu linguistic tokenizer.")

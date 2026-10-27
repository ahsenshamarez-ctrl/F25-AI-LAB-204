# Week 1 — Introduction to AI

**Name:** ____________________  
**Course/Section:** ____________________  
**Date:** ____________________

## 1. AI timeline

| Year | Event | Why it matters |
|---|---|---|
| 1950 | Alan Turing wrote about machine intelligence. | It raised the question of how we can test machine intelligence. |
| 1956 | Dartmouth AI workshop. | Artificial intelligence became established as a research field. |
| 1974–1980 | First AI winter (commonly dated period). | Progress was slower than expected, and interest and funding fell. |
| 1986 | A well-known paper on backpropagation was published. | It helped researchers train multi-layer neural networks. |
| 2012 | Deep learning achieved a major ImageNet result. | Large datasets and better computing helped neural networks improve. |
| 2017 | The Transformer paper was published. | Transformers became important for modern language models. |
| 2022 | ChatGPT was released publicly. | People could try a conversational AI tool directly. |

## 2. Simple scholarship rules

For this example, a student qualifies if their score is at least 70, their documents are complete, attendance is at least 75%, and they pass the interview. These are made-up rules for this lab, not a real university policy.

```python
def check_scholarship(score, documents_complete, attendance, interview_passed):
    if score < 70:
        return False, "Score is below 70"
    if not documents_complete:
        return False, "Documents are incomplete"
    if attendance < 75:
        return False, "Attendance is below 75%"
    if not interview_passed:
        return False, "Interview was not passed"
    return True, "All conditions are satisfied"


tests = [
    ("Test 1", 85, True, 90, True, True),
    ("Test 2", 85, True, 70, True, False),
    ("Test 3", 85, True, 90, False, False),
    ("Test 4", 70, True, 75, True, True),
]

for name, score, docs, attendance, interview, expected in tests:
    result, reason = check_scholarship(score, docs, attendance, interview)
    print(name, "Expected:", expected, "Actual:", result, "-", reason)
```

## 3. Test results

| Test | Input | Expected | Actual |
|---|---|---|---|
| 1 | Score 85, documents complete, attendance 90%, interview passed | Pass | Pass |
| 2 | Score 85, documents complete, attendance 70%, interview passed | Fail | Fail |
| 3 | Score 85, documents complete, attendance 90%, interview not passed | Fail | Fail |
| 4 | Score 70, documents complete, attendance 75%, interview passed | Pass | Pass |

All four examples give the expected result. Test 4 checks the minimum score and attendance values.

## 4. Disagreement and improvement

There was no disagreement in the four tests. One problem is that the program does not check whether attendance is over 100%. I would improve it by checking that attendance is between 0 and 100 and that the score is in a valid range.

## 5. Conversational AI example

A conversational answer can sound good but still be wrong. For example, a student with a score of 69 might be told they qualify because their attendance and interview are good. Under the rules in this lab, they do not qualify because their score is below 70. This is an example written for the assignment, not a response from a real AI model.

A useful test is to give a system several applications and compare its answers with the rules. We should check both the decision and the reason. Passing a few tests does not prove that a system is always correct or generally intelligent.

## 6. Short reflection

The rule-based program is easy to understand because each condition is written clearly. Testing helps find mistakes, especially around minimum values. The program still needs better input checks. Real scholarship rules should also be fair, clear, and reviewed by people.

## References

1. A. M. Turing, “Computing Machinery and Intelligence,” *Mind*, 1950. https://doi.org/10.1093/mind/LIX.236.433
2. Dartmouth AI workshop proposal archive: https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html
3. Encyclopaedia Britannica, “Artificial intelligence”: https://www.britannica.com/technology/artificial-intelligence
4. D. E. Rumelhart, G. E. Hinton and R. J. Williams, “Learning representations by back-propagating errors,” *Nature*, 1986. https://doi.org/10.1038/323533a0
5. A. Krizhevsky, I. Sutskever and G. Hinton, “ImageNet Classification with Deep Convolutional Neural Networks,” NeurIPS, 2012: https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
6. A. Vaswani et al., “Attention Is All You Need,” NeurIPS, 2017: https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
7. OpenAI, “Introducing ChatGPT,” 2022: https://openai.com/index/chatgpt/

**Before submitting:** fill in your name, course and date, and make sure you can explain the code and the answers.

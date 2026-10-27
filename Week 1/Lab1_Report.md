# AI Lab 1

**Name:** ____________________  
**Course:** ____________________  
**Date:** ____________________

## 1. AI timeline

| Year | Event | Why it matters |
|---|---|---|
| 1950 | Alan Turing wrote about machine intelligence. | It raised the question of how we could test machine intelligence. |
| 1956 | Dartmouth AI workshop. | The term artificial intelligence became established as a research field. |
| 1974–1980 | First AI winter (commonly dated). | Progress was slower than expected and interest and funding fell. |
| 1986 | Backpropagation paper by Rumelhart, Hinton and Williams. | It helped researchers train multi-layer neural networks. |
| 2012 | Deep learning made a major ImageNet advance. | Large datasets and better computing helped neural networks improve. |
| 2017 | Transformer paper was published. | Transformers became important for modern language models. |
| 2022 | ChatGPT was released publicly. | Many people could try a conversational AI tool directly. |

## 2. Simple scholarship rules

For this lab, I used four conditions: score must be at least 70, documents must be complete, attendance must be at least 75%, and the interview must be passed. The thresholds are examples for the assignment, not an actual university policy.

The program checks one condition at a time and gives a reason if the student does not qualify.

### Four test cases

| Test | Input | Expected result | Actual result |
|---|---|---|---|
| 1 | Score 85, documents complete, attendance 90%, interview passed | Pass | Pass |
| 2 | Score 85, documents complete, attendance 70%, interview passed | Fail | Fail |
| 3 | Score 85, documents complete, attendance 90%, interview not passed | Fail | Fail |
| 4 | Score 70, documents complete, attendance 75%, interview passed | Pass | Pass |

All four cases gave the expected result. The fourth case checks that a student exactly on both minimum values is accepted.

## 3. Disagreement and improvement

There was no disagreement in the four tests. One issue is that the current program would accept an attendance value above 100% if the other conditions passed. A better version should check that attendance is between 0 and 100 and also check that the score is in a valid range.

## 4. Conversational AI example

A conversational answer can sound convincing but still be wrong. For example, a student with a score of 69 might be told they qualify because their attendance and interview are good. Under the rules in this lab, that answer is wrong because the score is below 70. This is a made-up example for explaining the problem, not a response from a real AI model.

A useful test is to give a system several applications and compare its decisions with the rules. We should also check whether it explains the correct reason. A few successful tests do not prove that a system is generally intelligent or always correct.

## 5. Short reflection

The rule-based program is easy to understand because its conditions are written clearly. Testing helps find mistakes, especially around the minimum values. However, the program needs better input checks, and real scholarship rules should be fair, clear and reviewed by people.

## References

1. A. M. Turing, “Computing Machinery and Intelligence,” *Mind*, 1950. https://doi.org/10.1093/mind/LIX.236.433
2. Dartmouth AI workshop proposal archive. https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html
3. Encyclopaedia Britannica, “Artificial intelligence.” https://www.britannica.com/technology/artificial-intelligence
4. D. E. Rumelhart, G. E. Hinton and R. J. Williams, “Learning representations by back-propagating errors,” *Nature*, 1986. https://doi.org/10.1038/323533a0
5. A. Krizhevsky, I. Sutskever and G. Hinton, “ImageNet Classification with Deep Convolutional Neural Networks,” NeurIPS, 2012. https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
6. A. Vaswani et al., “Attention Is All You Need,” NeurIPS, 2017. https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
7. OpenAI, “Introducing ChatGPT,” 2022. https://openai.com/index/chatgpt/

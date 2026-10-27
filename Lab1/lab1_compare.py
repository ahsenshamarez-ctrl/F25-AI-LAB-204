# A small example of how a fluent answer can still be incorrect.
# The conversational answer below is made up for the lab; it is not real model output.

from lab1_rules import check_scholarship

case = {
    "score": 69,
    "documents_complete": True,
    "attendance": 90,
    "interview_passed": True,
}

rule_result, reason = check_scholarship(**case)
chat_answer = "You qualify because your attendance and interview are good."
chat_result = True  # This answer forgets to check the score.

print("Input:", case)
print("Rule result:", "PASS" if rule_result else "FAIL")
print("Reason:", reason)
print("Example chat answer:", chat_answer)
print("Example chat result:", "PASS" if chat_result else "FAIL")
print("Do they agree?", rule_result == chat_result)
print("Note: this is an example, not output from a tested AI model.")

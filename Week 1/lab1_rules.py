# Simple scholarship eligibility example for AI Lab 1.
# These rules are made-up for the lab, not a real university policy.


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
    ("Test 1 - all conditions pass", 85, True, 90, True, True),
    ("Test 2 - attendance too low", 85, True, 70, True, False),
    ("Test 3 - interview not passed", 85, True, 90, False, False),
    ("Test 4 - minimum values", 70, True, 75, True, True),
]

if __name__ == "__main__":
    for name, score, documents, attendance, interview, expected in tests:
        result, reason = check_scholarship(score, documents, attendance, interview)
        print(name)
        print("Expected:", "PASS" if expected else "FAIL")
        print("Actual:  ", "PASS" if result else "FAIL")
        print("Reason:", reason)
        print("Correct:", result == expected)
        print()

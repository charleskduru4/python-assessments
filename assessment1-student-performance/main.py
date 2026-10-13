"""Assessment 1: Student Performance Management System."""

PASS_MARK = 45

# Student names and scores stored in a dictionary (name -> score).
# "Grace" has an invalid score on purpose to demonstrate validation.
students = {
    "John": 85,
    "Mary": 72,
    "Peter": 55,
    "Amina": 48,
    "Chidi": 39,
    "Zainab": 66,
    "Grace": 105,
}


def is_valid_score(score):
    """Return True if the score is a number between 0 and 100."""
    return isinstance(score, (int, float)) and 0 <= score <= 100


def get_grade(score):
    """Return the letter grade for a score using conditional statements."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def main():
    total = 0
    valid_count = 0
    passed = 0
    failed = 0
    invalid_entries = []

    print("Student Performance Report")
    print("--------------------------")

    for name, score in students.items():
        # Reject scores outside the 0-100 range
        if not is_valid_score(score):
            invalid_entries.append((name, score))
            continue

        grade = get_grade(score)
        print(f"Name: {name} | Score: {score} | Grade: {grade}")

        total += score
        valid_count += 1
        if score >= PASS_MARK:
            passed += 1
        else:
            failed += 1

    if valid_count > 0:
        average = total / valid_count
        print(f"Class Average: {average:.2f}")
    else:
        print("Class Average: N/A (no valid scores)")

    print(f"Students Passed: {passed}")
    print(f"Students Failed: {failed}")

    if invalid_entries:
        print("\nRejected Entries (score must be 0-100):")
        for name, score in invalid_entries:
            print(f"  {name}: {score}")


if __name__ == "__main__":
    main()

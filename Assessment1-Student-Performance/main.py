
# Student Performance Management System

# Store student names and scores using a dictionary.
students = {
    "John": 85,
    "Mary": 72,
    "Peter": 55,
    "Sarah": 43,
    "David": 67
}


def determine_grade(score):
    """Return a letter grade based on the student's score."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 70:
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
    total_score = 0
    passed = 0
    failed = 0
    valid_students = 0

    print("Student Performance Report")
    print("--------------------------")

    for name, score in students.items():
        # Reject scores outside the allowed range.
        if score < 0 or score > 100:
            print(f"Name: {name} | Score: {score} | Invalid score")
            continue

        grade = determine_grade(score)
        print(f"Name: {name} | Score: {score} | Grade: {grade}")

        total_score += score
        valid_students += 1

        if score >= 45:
            passed += 1
        else:
            failed += 1

    if valid_students > 0:
        average = total_score / valid_students
        print(f"\nClass Average: {average:.2f}")
    else:
        print("\nClass Average: N/A")

    print(f"Students Passed: {passed}")
    print(f"Students Failed: {failed}")


if __name__ == "__main__":
    main()

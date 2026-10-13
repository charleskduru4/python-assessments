# Assessment 1: Student Performance Management System

A Python program that stores student scores, assigns grades, and summarises class performance.

## Features
- Stores student names and scores in a dictionary
- `get_grade()` function assigns grades using `if/elif/else`:
  - 70–100: A | 60–69: B | 50–59: C | 45–49: D | 0–44: F
- Loops through students and prints name, score and grade
- Calculates the class average (valid scores only)
- Counts students who passed (score >= 45) and failed
- Rejects and reports scores outside 0–100

## How to Run
Requires Python 3.6+.

```bash
cd assessment1-student-performance
python main.py
```

## Sample Output
```
Student Performance Report
--------------------------
Name: John | Score: 85 | Grade: A
Name: Mary | Score: 72 | Grade: A
Name: Peter | Score: 55 | Grade: C
Name: Amina | Score: 48 | Grade: D
Name: Chidi | Score: 39 | Grade: F
Name: Zainab | Score: 66 | Grade: B
Class Average: 60.83
Students Passed: 5
Students Failed: 1

Rejected Entries (score must be 0-100):
  Grace: 105
```

Edit the `students` dictionary in `main.py` to try different data.

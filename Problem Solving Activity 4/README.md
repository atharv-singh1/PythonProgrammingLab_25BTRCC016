# Problem-Solving Activity 4 (PSA 4) - Debugging the Code
**Course:** Python Programming | **Semester:** III  
**Institution:** JAIN (Deemed-to-be University)  
**Department:** Computer Science and Engineering - Cybersecurity  
**Repository:** [PythonProgrammingLab_25BTRCC016](https://github.com/atharv-singh1/PythonProgrammingLab_25BTRCC016)

---

## Directory Overview

This repository contains the corrected, verified implementations and execution evidence for PSA 4.

| Question | File | Description | Output Screenshot |
| :--- | :--- | :--- | :--- |
| **Q1** | [`Q1_scholarship.py`](./Q1_scholarship.py) | Scholarship Eligibility (Precedence & Type Conversion) | [View Screenshot](./screenshots/Q1_scholarship_output.png) |
| **Q2** | [`Q2_prime_numbers.py`](./Q2_prime_numbers.py) | Prime Number Generation (Loop Bounds & Logic) | [View Screenshot](./screenshots/Q2_prime_numbers_output.png) |
| **Q3** | [`Q3_digit_sum.py`](./Q3_digit_sum.py) | Recursive Digit Sum (Return Value & Base Cases) | [View Screenshot](./screenshots/Q3_digit_sum_output.png) |
| **Q4** | [`Q4_marks_processing.py`](./Q4_marks_processing.py) | Marks Processing (List Mutation, Sorting, Slicing) | [View Screenshot](./screenshots/Q4_marks_processing_output.png) |
| **Q5** | [`Q5_common_courses.py`](./Q5_common_courses.py) | Common Courses Analysis (Sets, Dictionaries) | [View Screenshot](./screenshots/Q5_common_courses_output.png) |

---

## Question Details & Error Diagnosis

### Question 1: Operator Precedence, Type Conversion and Conditional Reasoning
- **Errors Identified:**
  1. `average = m1 + m2 + m3 / 3` suffers from operator precedence (`/` has higher precedence than `+`), dividing only `m3` by 3 instead of the sum.
  2. Input read via `input().split()` produces string values; performing mathematical operations without `float()` or `int()` conversion leads to errors.
  3. The condition `m1 >= 40 and m2 >= 40 or m3 >= 40` mistakenly used `or`, allowing a student to pass even if failing one subject. It must require `and` across all three marks.
- **Verification & Test Cases:**
  - `80 70 90 85` → `Average: 80.0`, `Status: Eligible`
  - `35 90 90 85` → `Average: 71.67`, `Status: Not Eligible`

---

### Question 2: Nested Loops, Loop Control and Prime Number Generation
- **Errors Identified:**
  1. `range(start, end)` excludes the `end` boundary; it must be `range(start, end + 1)` for an inclusive range.
  2. Divisor range `range(2, int(number ** 0.5))` excludes the square root itself due to Python's upper-bound exclusion (e.g., fails for 4, 9, 25); needs `+ 1`.
  3. When a divisor is found, `continue` was used instead of `break`, causing unnecessary iterations and overwriting `is_prime` without exiting early.
- **Verification & Test Cases:**
  - `generate_primes(1, 30)` → `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`
  - `generate_primes(2, 2)` → `[2]`
  - `generate_primes(14, 16)` → `[]`
  - `generate_primes(9, 9)` → `[]`

---

### Question 3: Recursion, Base Cases and Function Return Values
- **Errors Identified:**
  1. The recursive call `digit_sum(number // 10)` did not capture or return the recursive result; it discarded the computed sum.
  2. The function only returned `digit` (`number % 10`), yielding only the last digit rather than the cumulative sum.
  3. The base case `if number < 10: return number` works for single digits, but intermediate aggregation required combining `digit + digit_sum(number // 10)`.
- **Verification & Test Cases:**
  - `digit_sum(5824)` → `19`
  - `digit_sum(7)` → `7`
  - `digit_sum(0)` → `0`

---

### Question 4: Lists, Mutation, Comprehensions and Sorting
- **Errors Identified:**
  1. Modifying a list (`marks.remove(mark)`) while iterating over it with a `for` loop skips adjacent elements due to index shifting.
  2. `unique_marks.sort(reverse=True)` sorted descending, contradicting Requirement 3 (ascending order).
  3. `mark > 60` excluded marks equal to 60, violating Requirement 4 (greater than or equal to 60).
- **Verification & Test Cases:**
  - Input: `[35, 60, 45, 80, 35, 55, 60, 95, 40, 80]`
  - Processed: `[40, 45, 55, 60, 80, 95]`
  - Qualified: `[60, 80, 95]`
  - Top three: `[95, 80, 60]`

---

### Question 5: Dictionaries, Sets, Nested Data and Data Consistency
- **Errors Identified:**
  1. The threshold `len(common) > 2` required at least 3 shared courses, missing students sharing exactly 2 courses. It must be `>= 2`.
  2. Lists in dictionary contained duplicate entries (e.g. `["Python", "Java", "SQL", "Python"]`); converting both lists to sets ensures accurate distinct intersections.
  3. The set elements were converted directly to `list(common)` without sorting, yielding non-deterministic element order; alphabetical sorting via `sorted(common)` ensures consistency.
- **Verification & Test Cases:**
  - Output: `{'Bala': ['Python', 'SQL'], 'Charan': ['Java', 'Python', 'SQL'], 'Divya': ['Java', 'Python']}`

---

## Execution Screenshots

All test runs are documented in the `screenshots/` directory:
- `screenshots/Q1_scholarship_output.png`
- `screenshots/Q2_prime_numbers_output.png`
- `screenshots/Q3_digit_sum_output.png`
- `screenshots/Q4_marks_processing_output.png`
- `screenshots/Q5_common_courses_output.png`

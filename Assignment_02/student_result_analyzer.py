names = ["Arun", "Bala", "Charan", "Divya", "Esha"]
marks = [85, 72, 38, 105, 91]

valid_students = 0

for number, (name, mark) in enumerate(zip(names, marks), start=1):
    if mark < 0 or mark > 100:
        print(f"Invalid marks for {name} - Skipped")
        continue

    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    elif mark >= 40:
        result = "Average"
    else:
        result = "Fail"

    print(f"{number}. {name} - {mark} - {result}")
    valid_students += 1

print(f"\nTotal Valid Students: {valid_students}")

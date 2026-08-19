names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]
attendance = [92, 68, 85, 45, 78]
marks = [88, 55, 76, 32, 91]

eligible_students = 0

for number, (name, att, mark) in enumerate(zip(names, attendance, marks), start=1):
    if att < 0 or att > 100 or mark < 0 or mark > 100:
        print(f"Invalid data for {name} - Skipped")
        continue

    if att >= 75:
        if mark >= 80:
            result = "Distinction"
        elif mark >= 60:
            result = "First Class"
        elif mark >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print(f"{number}. {name} - Attendance: {att}% - Marks: {mark} - {result}")
        eligible_students += 1
    else:
        print(f"{number}. {name} - Attendance: {att}% - Not Eligible")

print(f"Total Eligible Students: {eligible_students}")

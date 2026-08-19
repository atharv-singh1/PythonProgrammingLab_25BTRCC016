student_name = input("Enter student name: ")
usn = input("Enter USN: ")

mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))
mark4 = float(input("Enter marks in subject 4: "))
mark5 = float(input("Enter marks in subject 5: "))

total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total_marks / 5
average = total_marks / 5

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "RA"

print("\n========== STUDENT PERFORMANCE REPORT ==========")
print(f"Student Name: {student_name}")
print(f"USN: {usn}")
print("------------------------------------------------")
print(f"Total Marks: {total_marks} / 500")
print(f"Percentage: {percentage}%")
print(f"Average: {average}")
print(f"Grade: {grade}")

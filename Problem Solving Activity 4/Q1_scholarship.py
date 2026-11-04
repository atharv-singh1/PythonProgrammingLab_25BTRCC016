def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3
    if (m1 >= 40 and m2 >= 40 and m3 >= 40
            and average >= 75 and attendance >= 75):
        return average, "Eligible"
    return average, "Not Eligible"


marks = list(map(float, input("Enter 3 marks and attendance: ").split()))
average, status = evaluate(marks[0], marks[1], marks[2], marks[3])
print("Average:", round(average, 2))
print("Status:", status)

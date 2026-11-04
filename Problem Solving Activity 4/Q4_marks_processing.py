marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]

processed = sorted(set(mark for mark in marks if mark >= 40))
qualified = [mark for mark in processed if mark >= 60]
top_three = sorted(qualified, reverse=True)[:3]

print("Processed marks:", processed)
print("Qualified marks:", qualified)
print("Top three:", top_three)

# Extra test: fewer than three qualifying marks
extra = [39, 40, 60, 60]
extra_processed = sorted(set(x for x in extra if x >= 40))
extra_qualified = [x for x in extra_processed if x >= 60]
print("Extra top:", sorted(extra_qualified, reverse=True)[:3])

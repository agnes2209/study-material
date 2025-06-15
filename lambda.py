#lambda arguments: expression

students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]

# sort by score
students.sort(key=lambda student: student[1])
print("Sorted students by score:", students)
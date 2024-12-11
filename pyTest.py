# Step 1: Initialize an empty list to store grades
grades = []

# Step 2: Use a for loop to collect grades
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    grade = float(input(f"Enter grade for student {i + 1}: "))
    grades.append(grade)

# Step 3: Use a for loop to print all the grades
print("\nGrades entered:")
for grade in grades:
    print(grade)

# Step 4: Use a for loop to calculate the average of the grades
total = 0
for grade in grades:
    total += grade

average = total / len(grades)
print(f"\nThe average grade is: {average:.2f}")

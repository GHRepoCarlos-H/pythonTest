# # Step 1: Initialize an empty list to store grades
# grades = []

# # Step 2: Use a for loop to collect grades
# num_students = int(input("Enter the number of students: "))
# for i in range(num_students):
#     grade = float(input(f"Enter grade for student {i + 1}: "))
#     grades.append(grade)

# # Step 3: Use a for loop to print all the grades
# print("\nGrades entered:")
# for grade in grades:
#     print(grade)

# # Step 4: Use a for loop to calculate the average of the grades
# total = 0
# for grade in grades:
#     total += grade

# average = total / len(grades)
# print(f"\nThe average grade is: {average:.2f}")

# count = 0
# while count < 5:
#     print("Count is: ", count)
#     count += 1

# for i in range(1, 6, 2):
#     print(i)

# count=0
# while count < 5:
#     print(f"your count is: {count}")
#     count += 1

# multiply=int(input("Enter number to multiply by 2: "))
# print(f'You total multiplied by two is {multiply * 2}')

# for i in range(5, 12, 2):
#     print(i)

# count=10
# while count <= 20:
#     print(f"your number is: {count}")
#     count += 1

# total = 0
# for i in range(1, 11):
#     total += i
#     print(f"After adding {i}, total now is: {total}")
# print("The sum of all numbers is: ", total)


# total=0
# for i in range(1, 11):
#     total += i
#     print({i}, {total})
# print(total)

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# for fruit in fruits:
#     print(fruit)

# for i in range(2, 11, 2):
#     print(i)

# y=2
# x=(int(input('Enter a number: ')))
# z=(x+y)
# print(f"The total is:", z)

# n1=(int(input('Enter your first number: ')))
# task=(input("Enter an operator: "))
# n2=(int(input('Enter your second number: ')))
# result = eval(f'{n1} {task} {n2}')
# print(f'your total is: ', result)

while True:
    n1 = int(input('Enter your first number: '))
    task = input("Enter an operator (+, -, *, /): ")
    n2 = int(input('Enter your second number: '))

    try:
        result = eval(f'{n1} {task} {n2}')
        print(f'Your total is: {result}')
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except:
        print("Invalid input. Please enter valid numbers and operators.")
    
    # Ask if the user wants another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Goodbye!")
        break

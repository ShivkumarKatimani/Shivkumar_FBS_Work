students = int(input("Enter number of students: "))

total_percentage = 0

for i in range(students):

    total = 0

    print("Student", i + 1)

    for j in range(5):
        marks = float(input("Enter marks: "))
        total += marks

    percentage = total / 5

    print("Percentage =", percentage)

    total_percentage += percentage

average = total_percentage / students

print("Average Percentage =", average)
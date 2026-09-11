# Day 5 - Student Marks Program
# Store marks for five students and calculate average and grade.

students = {
    "Student 1": [85, 78, 92],
    "Student 2": [70, 75, 68],
    "Student 3": [95, 90, 93],
    "Student 4": [60, 65, 58],
    "Student 5": [80, 82, 79]
}


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


for student, marks in students.items():
    average = sum(marks) / len(marks)
    grade = get_grade(average)

    print(student)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print()

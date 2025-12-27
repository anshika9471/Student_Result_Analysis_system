import csv
import os

FILE_NAME = "students_result.csv"

def get_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    else:
        return 0

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    subjects = ["Maths", "Physics", "Chemistry",
                "English", "Computer", "Electronics"]

    marks = []
    grade_points = []

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)
        grade_points.append(get_grade_point(mark))

    total = sum(marks)
    percentage = round(total / len(subjects), 2)
    cgpa = round(sum(grade_points) / len(subjects), 2)

    if cgpa >= 9:
        grade = " A+"
    elif cgpa >= 8:
        grade = " A"
    elif cgpa >= 7:
        grade = " B"
    elif cgpa >= 6:
        grade = " C"
    else:
        grade = " Fail"

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                ["RollNo", " Name",
                 " Maths ", " Physics ", " Chemistry ", " English ", " Computer ", " Electronic" "Total", " Percentage", " CGPA", " Grade"]
            )

        writer.writerow([roll, name] + marks + [total, percentage, cgpa, grade])

    print(" Student result added successfully!")

def view_results():
    if not os.path.exists(FILE_NAME):
        print(" No records found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))

def main_menu():
    while True:
        print("\n----- Student Result Analysis System -----")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_results()
        elif choice == "3":
            print(" Exiting program")
            break
        else:
            print(" Invalid choice. Try again.")

main_menu()


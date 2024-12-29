from tabulate import tabulate

# Initialize an empty list to store student records
students = []

def add_student():
    """Add a new student to the table."""
    print("\nAdd a new student:")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    student_code = input("Enter Student Code: ")
    graduation_year = input("Enter Graduation Year: ")

    # Append the student details as a dictionary to the students list
    students.append({
        "First Name": first_name,
        "Last Name": last_name,
        "Student Code": student_code,
        "Graduation Year": graduation_year
    })
    print("\nStudent added successfully!\n")

def display_students():
    """Display the table of students."""
    if not students:
        print("\nNo students in the table yet.\n")
    else:
        print("\nStudent Records:")
        print(tabulate(students, headers="keys", tablefmt="grid"))
        print()

def main():
    """Main program to manage the student table."""
    while True:
        print("Student Table Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, roll_number, grade):
        # Constructor to initialize student attributes
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        # Constructor to initialize the list of students
        self.students = []

    def add_student(self, name, roll_number, grade):
        # Method to add a new student to the system
        new_student = Student(name, roll_number, grade)
        self.students.append(new_student)

    def view_all_students(self):
        # Method to display details of all students in the system
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

    def search_student_by_number(self, roll_number):
        # Method to search for a student by roll number and display details
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
                return
        print("Student not found with the given roll number.")

    def update_student_grade(self, roll_number, new_grade):
        # Method to update a student's grade based on roll number
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print(f"Grade updated for {student.name} (Roll Number: {student.roll_number}) to {new_grade}.")
                return
        print("Student not found with the given roll number.")

def main():
    # Create an instance of the StudentManagementSystem
    student_system = StudentManagementSystem()

    while True:
        # Display the menu options
        print("\nStudent Management System Menu:")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student by number")
        print("4. Update a student's grade")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Adding a new student
            name = input("Enter the student's name: ")
            roll_number = input("Enter the student's roll number: ")
            grade = input("Enter the student's grade: ")
            student_system.add_student(name, roll_number, grade)

        elif choice == "2":
            # View all students
            student_system.view_all_students()

        elif choice == "3":
            # Search for a student by roll number
            roll_number = input("Enter the roll number to search: ")
            student_system.search_student_by_number(roll_number)

        elif choice == "4":
            # Update a student's grade
            roll_number = input("Enter the roll number to update grade: ")
            new_grade = input("Enter the new grade: ")
            student_system.update_student_grade(roll_number, new_grade)

        elif choice == "5":
            # Exit the program
            print("Exiting the program.")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

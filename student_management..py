# Abstract base class for common person information
from abc import ABC, abstractmethod
import csv


# Person class provides common properties for all people
class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Every child class must implement this method
    @abstractmethod
    def display_info(self):
        pass


# Student class inherits common properties from Person
class Student(Person):

    def __init__(self, student_id, name, age, standard, marks):

        # Call the constructor of the parent class
        super().__init__(name, age)

        # Private attributes for student record
        self.__student_id = student_id
        self.__standard = standard
        self.__marks = marks

    # Implementation of the abstract method
    def display_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self._name)
        print("Age:", self._age)
        print("Standard:", self.__standard)
        print("Marks:", self.__marks)

    # Getter for marks
    def get_marks(self):
        return self.__marks

    # Setter to change or validate marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 to 100")

    # Getter for Student ID
    def get_student_id(self):
        return self.__student_id

    # Getter for Standard
    def get_standard(self):
        return self.__standard


# Student Management class handles all student records
class Student_Management:

    def __init__(self):
        self.students = []

    # Add a new student to the list
    def add_student(self):
        try:
            student_id = int(input("Enter the ID: "))
            name = input("Enter the Name: ")
            age = int(input("Enter the age: "))
            standard = input("Enter the Standard: ")
            marks = float(input("Enter the Marks: "))

            student = Student(student_id, name, age, standard, marks)
            self.students.append(student)

            print("Student added successfully.")

        except ValueError:
            print("Please enter valid numeric values.")

    # Display all stored students
    def display_students(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students:
            student.display_info()
            print()

    # Search for a student using Student ID
    def search_student(self):
        student_id = int(input("Enter the ID to search: "))

        for student in self.students:
            if student.get_student_id() == student_id:
                student.display_info()
                return

        print("Student not found.")

    # Update marks of an existing student
    def update_student(self):
        student_id = int(input("Enter the ID to update: "))

        for student in self.students:
            if student.get_student_id() == student_id:
                new_marks = float(input("Enter the new marks: "))
                student.set_marks(new_marks)
                print("Student marks updated successfully.")
                return

        print("Student not found.")

    # Delete a student using Student ID
    def delete_student(self):
        student_id = int(input("Enter student ID to delete: "))

        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    # Calculate the average marks of all students
    def calculate_avg(self):
        if not self.students:
            print("No students available.")
            return

        total = 0

        for student in self.students:
            total += student.get_marks()

        average = total / len(self.students)
        print("Average Marks:", average)

    # Save student records to CSV file
    def save_records(self):
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["Student_ID", "Name", "Age", "Standard", "Marks"]
            )

            for student in self.students:
                writer.writerow([
                    student.get_student_id(),
                    student._name,
                    student._age,
                    student.get_standard(),
                    student.get_marks()
                ])

        print("Records saved successfully.")

    # Load student records from CSV file
    def load_records(self):
        try:
            with open("students.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    student = Student(
                        int(row["Student_ID"]),
                        row["Name"],
                        int(row["Age"]),
                        row["Standard"],
                        float(row["Marks"])
                    )

                    self.students.append(student)

            print("Records loaded successfully.")

        except FileNotFoundError:
            print("students.csv file not found.")

    # Display menu and run the selected operation
    def menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Calculate Average Marks")
            print("7. Save Records")
            print("8. Load Records")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.calculate_avg()

            elif choice == "7":
                self.save_records()

            elif choice == "8":
                self.load_records()

            elif choice == "9":
                print("Program ended.")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the Student Management System
system = Student_Management()
system.menu()



from abc import ABC, abstractmethod
import csv
import os

class Person(ABC):

    def __init__(self, roll_no, name):
        self.__roll_no = roll_no
        self.__name = name

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def display(self):
        pass

class Student(Person):

    def __init__(self, roll_no, name, marks):
        super().__init__(roll_no, name)
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("\nStudent Details")
        print("-------------------------")
        print("Roll No :", self.get_roll_no())
        print("Name    :", self.get_name())
        print("Marks   :", self.__marks)

class StudentManager:

    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "students.csv")

    def add_student(self):

        try:
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks: "))

            student = Student(roll_no, name, marks)

            file_exists = os.path.isfile(self.filename)

            with open(self.filename, "a", newline="") as file:

                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(["Roll No", "Name", "Marks"])

                writer.writerow([
                    student.get_roll_no(),
                    student.get_name(),
                    student.get_marks()
                ])

            print("\nStudent Added Successfully.")

        except ValueError:
            print("Invalid Marks!")

    def display_students(self):

        try:
            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                data = list(reader)

                if len(data) <= 1:
                    print("\nNo Student Records Found.")
                    return

                print("\n========== Student Records ==========\n")

                for row in data[1:]:
                    print(f"Roll No : {row[0]}")
                    print(f"Name    : {row[1]}")
                    print(f"Marks   : {row[2]}")
                    print("----------------------------")

        except FileNotFoundError:
            print("\nNo Student Records Found.")  

    def search_student(self):

        try:
            roll = input("Enter Roll Number to Search: ")

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                next(reader)

                found = False

                for row in reader:

                    if row[0] == roll:
                        print("\nStudent Found")
                        print("---------------------")
                        print("Roll No :", row[0])
                        print("Name    :", row[1])
                        print("Marks   :", row[2])
                        found = True
                        break

                if not found:
                    print("Student Not Found.")

        except FileNotFoundError:
            print("No Student Records Found.")      

    def update_student(self):

        try:
            roll = input("Enter Roll Number to Update: ")

            rows = []

            found = False

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                rows = list(reader)

            for i in range(1, len(rows)):

                if rows[i][0] == roll:

                    print("\nStudent Found")

                    rows[i][1] = input("Enter New Name: ")
                    rows[i][2] = input("Enter New Marks: ")

                    found = True
                    break

            if found:

                with open(self.filename, "w", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerows(rows)

                print("Student Updated Successfully.")

            else:
                print("Student Not Found.")

        except FileNotFoundError:
            print("No Student Records Found.")

        except Exception:
            print("Something went wrong.")        


    def delete_student(self):

        try:

            roll = input("Enter Roll Number to Delete: ")

            rows = []

            found = False

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                rows = list(reader)

            new_rows = [rows[0]]

            for row in rows[1:]:

                if row[0] == roll:
                    found = True
                else:
                    new_rows.append(row)

            if found:

                with open(self.filename, "w", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerows(new_rows)

                print("Student Deleted Successfully.")

            else:
                print("Student Not Found.")

        except FileNotFoundError:
            print("No Student Records Found.")

    def calculate_average(self):

        try:

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                next(reader)

                total = 0
                count = 0

                for row in reader:

                    total += float(row[2])
                    count += 1

                if count == 0:
                    print("No Student Records Found.")
                else:
                    average = total / count
                    print(f"Average Marks = {average:.2f}")

        except FileNotFoundError:
            print("No Student Records Found.")


manager = StudentManager()

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            manager.add_student()

        elif choice == 2:
            manager.display_students()

        elif choice == 3:
            manager.search_student()

        elif choice == 4:
            manager.update_student()

        elif choice == 5:
            manager.delete_student()

        elif choice == 6:
            manager.calculate_average()

        elif choice == 7:
            print("\nThank You!")
            print("Exiting Student Management System...")
            break

        else:
            print("Invalid Choice!")
            
    except ValueError:
        print("Please enter a valid number .")
        
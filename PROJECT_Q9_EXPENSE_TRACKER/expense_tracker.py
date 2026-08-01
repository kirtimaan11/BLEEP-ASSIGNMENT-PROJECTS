from abc import ABC, abstractmethod
import csv
import os

class Record(ABC):

    def __init__(self, category, amount):
        self.__category = category
        self.__amount = amount

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def display(self):
        pass

class Expense(Record):

    def __init__(self, record_type, category, amount):
        super().__init__(category, amount)
        self.__record_type = record_type

    def get_record_type(self):
        return self.__record_type

    def set_record_type(self, record_type):
        self.__record_type = record_type

    def display(self):
        print("\nExpense Details")
        print("-----------------------")
        print("Type     :", self.__record_type)
        print("Category :", self.get_category())
        print("Amount   :", self.get_amount())

class ExpenseManager:

    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "expenses.csv")

    def add_record(self):

        try:

            record_type = input("Enter Type (Income/Expense): ")
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))

            expense = Expense(record_type, category, amount)

            file_exists = os.path.isfile(self.filename)

            with open(self.filename, "a", newline="") as file:

                writer = csv.writer(file)

                if os.path.getsize(self.filename) == 0:
                    writer.writerow(["Type", "Category", "Amount"])

                writer.writerow([
                    expense.get_record_type(),
                    expense.get_category(),
                    expense.get_amount()
                ])

            print("Record Added Successfully.")

        except ValueError:
            print("Invalid Amount.")

    def display_records(self):

        try:

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                data = list(reader)

                if len(data) <= 1:
                    print("\nNo Records Found.")
                    return

                print("\n========== Expense Records ==========\n")

                for row in data[1:]:

                    print("Type     :", row[0])
                    print("Category :", row[1])
                    print("Amount   :", row[2])
                    print("----------------------------")

        except FileNotFoundError:
            print("No Records Found.")

    def search_category(self):

        try:

            category = input("Enter Category to Search: ")

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                next(reader)

                found = False

                for row in reader:

                    if row[1].lower() == category.lower():

                        print("\nRecord Found")
                        print("--------------------")
                        print("Type     :", row[0])
                        print("Category :", row[1])
                        print("Amount   :", row[2])

                        found = True

                if not found:
                    print("No Record Found.")

        except FileNotFoundError:
            print("No Records Found.")


    def monthly_summary(self):

        try:

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                next(reader)

                income = 0
                expense = 0

                for row in reader:

                    if row[0].lower() == "income":
                        income += float(row[2])

                    elif row[0].lower() == "expense":
                        expense += float(row[2])

                print("\n====== Monthly Summary ======")
                print("Total Income  :", income)
                print("Total Expense :", expense)
                print("Balance       :", income - expense)

        except FileNotFoundError:
            print("No Records Found.")


manager = ExpenseManager()

while True:

    print("\n========== Expense Tracker ==========")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Category")
    print("4. Monthly Summary")
    print("5. Exit")

    try:

        choice = int(input("Enter Choice: "))

        if choice == 1:
            manager.add_record()

        elif choice == 2:
            manager.display_records()

        elif choice == 3:
            manager.search_category()

        elif choice == 4:
            manager.monthly_summary()

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please Enter a Valid Number.")    
            
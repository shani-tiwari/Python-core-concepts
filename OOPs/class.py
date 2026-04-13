# class is a blueprint/template of an object
# object is an instance of a class

# class is a user defined data type 
# it contains attributes(variables inside class) and methods(functions inside class)


# 1st example 
class First : 
    a = 10 # attributes
    def hello(): # method
        print("Hello class")

# creating objects
obj1 = First().hello()

# calling functions
print(First().a)

"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, 
total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes 
and its description. The same goes for expenses."""

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        return sum(income["amount"] for income in self.incomes)

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expense: {self.total_expense()}\n"
            f"Account Balance: {self.account_balance()}"
        )


# Example
person = PersonAccount("Shani", "Kumar")
person.add_income(50000, "Salary")
person.add_income(10000, "Freelance")
person.add_expense(15000, "Rent")
person.add_expense(5000, "Food")

print(person.account_info())
print(person.incomes)
print(person.expenses)

class Human:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def display_human_info(self):
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Employee:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"{self.name} works at {self.company}")


class Developer(Employee, Human):  # Multiple Inheritance
    def __init__(self, name, salary, company, age, gender, programming_language):
        Employee.__init__(self, name, salary, company)
        Human.__init__(self, age, gender)
        self.programming_language = programming_language

    def show_role(self):
        print(f"{self.name} is a Developer working with {self.programming_language}.")


# Creating objects
dev1 = Developer("Anand", 450000, "Cognizant", 25, "Male", "Java")
dev2 = Developer("Abhinav", 900000, "DeepTek", 28, "Male", "Python")

# Displaying details
dev1.display_details()
dev1.display_human_info()
dev1.show_role()

print()

dev2.display_details()
dev2.display_human_info()
dev2.show_role()

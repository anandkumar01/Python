# Base class
class Employee:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def display_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"{self.name} works in {self.company}")


# Derived class (Single Inheritance)
class Developer(Employee):
    def __init__(self, name, salary, company, bonus):
        super().__init__(name, salary, company)
        self.bonus = bonus

    def bonus_details(self):
        print(f"{self.get_name()} gets a bonus of {self.bonus} yearly")

    def calculate_salary(self):
        total_salary = self.get_salary() + self.bonus
        return total_salary


# Derived class (Multilevel Inheritance)
class BackendDeveloper(Developer):
    def __init__(self, name, salary, company, bonus, role):
        super().__init__(name, salary, company, bonus)
        self.role = role

    def project_role(self):
        print(f"{self.get_name()} works as a {self.role}")


# Main function to test the classes
if __name__ == "__main__":
    # Single Inheritance
    anand = Developer("Anand", 450000, "Cognizant", 50000)
    abhinav = Developer("Abhinav", 900000, "DeepTek", 80000)

    anand.display_details()
    anand.bonus_details()
    print(f"{anand.get_name()} gets salary after bonus: {anand.calculate_salary()}\n")

    abhinav.display_details()
    abhinav.bonus_details()
    print(f"{abhinav.get_name()} gets salary after bonus: {abhinav.calculate_salary()}\n")

    # Multilevel Inheritance
    ayush = BackendDeveloper("Ayush", 400000, "Accenture", 50000, "Backend Developer")
    ayush.display_details()
    ayush.project_role()

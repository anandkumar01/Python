# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee salary: {self.salary}")


# Derived class (Overriding display_details method)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Calling superclass constructor
        self.department = department

    # Overriding the display_details() method
    def display_details(self):
        super().display_details()  # Calling superclass method
        print(f"Manager Department: {self.department}")


# Main function to test the classes
if __name__ == "__main__":
    employee = Employee("Anand", 30000.00)
    manager = Manager("Sachin", 50000.00, "IT Department")

    print("Employee details:")
    employee.display_details()

    print("\nManager details:")
    manager.display_details()

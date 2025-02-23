from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

    @abstractmethod
    def project_deployment(self):
        pass  # Abstract method must be implemented in child class

    def project_details(self):
        print(f"{self.name} is allocated to {self.project} project")

    def display_info(self):
        print(f"{self.name} is {self.age} years old and salary is {self.salary}")


# Concrete class inheriting from Employee
class Developer(Employee):
    def __init__(self, name, age, salary, project):
        super().__init__(name, age, salary, project)

    def project_deployment(self):
        print("Project deployment has been done")


# Main function to test the classes
if __name__ == "__main__":
    developer = Developer("Anand", 24, 30000, "NSE Fots T&M")
    developer.display_info()
    developer.project_details()
    developer.project_deployment()

class Employee:
    def __init__(self, name, emp_id, salary, designation):
        # Private attributes (Encapsulation)
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary
        self.__designation = designation

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getter and Setter for emp_id
    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter and Setter for salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    # Getter and Setter for designation
    @property
    def designation(self):
        return self.__designation

    @designation.setter
    def designation(self, designation):
        self.__designation = designation


# Main function to test the class
if __name__ == "__main__":
    # Creating an object of Employee
    anand = Employee("Anand", 12345, 450399.0, "Software Developer")

    # Using getters to access private attributes
    print("Employee name:", anand.name)
    print("Employee ID:", anand.emp_id)
    print("Employee salary:", anand.salary)
    print("Employee designation:", anand.designation)

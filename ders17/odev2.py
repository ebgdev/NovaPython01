class Employee:
    def __init__(self, name, base_salary):
        self._name = name  # Private attribute
        self._base_salary = base_salary

    def calculate_salary(self):  # Polymorphic method
        return self._base_salary

    def display_info(self):
        print(f"Employee: {self._name}, Salary: {self.calculate_salary()}")


class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self._bonus = bonus  # Private attribute

    def calculate_salary(self):  # Method overriding
        return self._base_salary + self._bonus


class Manager(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)
        self._commission = commission  # Private attribute

    def calculate_salary(self):  # Method overriding
        return self._base_salary + self._commission


class Company:
    def __init__(self):
        self._employees = {}  # Private dictionary to store employees

    def add_employee(self, employee):
        self._employees[employee._name] = employee

    def display_all_salaries(self):
        print("\nEmployee Salaries:")
        for emp_name, employee in self._employees.items():
            employee.display_info()


# Usage
company = Company()
developer = Developer("Alice", 50000, 10000)
manager = Manager("Bob", 60000, 15000)

# Add employees using a loop
for emp in [developer, manager]:
    company.add_employee(emp)

# Display all employee salaries
company.display_all_salaries()


print(developer._name)
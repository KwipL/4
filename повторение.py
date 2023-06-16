class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
employee = Employee(name='qwerty', salary = 120)
print(f'У {employee.name} зарплата составляет {employee.salary} биткоинов')
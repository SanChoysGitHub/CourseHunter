from classes import Person, Employee

person = Person('Katy', 30)
person.age = 35
person.print_info()

employee = Employee('Job', 25, 'Google')
employee.print_info()
employee.more_info()
employee.__str__()
print(employee)













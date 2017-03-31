#!/usr/bin/env python3

class Emplyee:
    'hello'
    empCount = 0
    __heh = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Emplyee.empCount += 1
        self.__hh = 0

    def displayCount(self):
        print('Total employee %d' % Emplyee.empCount)

    def displayEmployee(self):
        print('Name: %s, Salary: %s' % (self.name, self.salary))

    def display(self):
        print('Total: {}'.format(Emplyee.empCount))
        print('Name: {}; Salary: {}'.format(self.name, self.salary))
        print('Name: {0}; Salary: {1}'.format(self.name, self.salary))
        print('Name: {name}; Salary: {salary}'.format(name=self.name, salary=self.salary))

    def __func(self):
        pass

print("Employee.__doc__:", Emplyee.__doc__)
print("Employee.__name__:", Emplyee.__name__)
print("Employee.__module__:", Emplyee.__module__)
print("Employee.__bases__:", Emplyee.__bases__)
print("Employee.__dict__:", Emplyee.__dict__)

# e = Emplyee('aa', 'xx')
# e.displayCount()
# e.displayEmployee()
# e.display()

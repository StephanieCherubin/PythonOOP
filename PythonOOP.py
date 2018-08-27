class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '@' + last + '.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Shiela', 'Pierre', 80000)
emp_2 = Employee('Taylor', 'Law', 70000)

emp_string_1 = 'Joanna-Dias-50000'
emp_string_2 = 'Kellie-Lopez-85000'
emp_string_3 = 'Nancy-Martin-40000'

new_emp_1 = Employee.from_string(emp_string_1)

print(new_emp_1.email)
print(new_emp_1.pay)
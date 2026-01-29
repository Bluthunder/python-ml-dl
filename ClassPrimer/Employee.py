
class Employee:

    nums_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@demo.com'
        self.pay = pay

        Employee.nums_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'



    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    raise_amount = 1.14

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())






emp_1 = Employee('Kaushik', 'Roy', 90000)
emp_2 = Employee('Jojo', 'Roy', '80900')

emp_str = 'Steve-Smith-70000'

emp_3 = Employee.from_string(emp_str)

dev_1 = Developer('Kaushik', 'Roy', 90000, "Python")

mng_1 = Manager('Jojo', 'Roy', '80900', [dev_1])

print(dev_1.prog_lang)

print(mng_1.email)

mng_1.print_emps()
# print(emp_2)
# print(emp_3)
#
# print(emp_3.email)

#
# emp_1.first = 'Kaushik'
# emp_1.last = 'Roy'
# emp_1.email = 'Test@demo.com'
# emp_1.pay = 50000
#
#
# emp_2.first = 'Jojo'
# emp_2.last = 'Roy'
# emp_2.email = 'Test1@demo.com'
# emp_2.pay = 40000

#
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.raise_amount)

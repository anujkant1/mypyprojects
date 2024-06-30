import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@dc.com'
        Employee.num_of_emps += 1
    
    def fullname(self):
        return (f'{self.fname} {self.lname}')
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    
dev_1 = Developer('Clark', 'Kent', 90000)
dev_2 = Developer('Bruce', 'Wayne', 180000)

print(dev_1.fullname())
print(dev_2.fullname())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
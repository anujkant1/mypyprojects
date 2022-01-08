import datetime


class Employee:

    emp_count = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay) -> None:
        self.fname = str(fname).capitalize()
        self.lname = str(lname).capitalize()
        self.alias = ('a' + fname[0:3] + lname[0:3]).lower()
        self.pay = int(pay)
        self.email = (self.fname + '.' + self.lname + '@acompany.com').lower()

        Employee.emp_count += 1

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def __repr__(self) -> str:
        return f'''Employee: {self.fullname()}
          alias: {self.alias}
          email: {self.email}'''

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str):  # Alternate constructor
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, fname, lname, pay, language) -> None:
        super().__init__(fname, lname, pay)
        self.language = language.capitalize()  # Programming language specialization


class Manager(Employee):

    def __init__(self, fname, lname, pay, reportees=None) -> None:
        super().__init__(fname, lname, pay)
        if reportees is None:
            self.reportees = []
        else:
            self.reportees = reportees

    def add_reportee(self, emp):
        if emp not in self.reportees:
            self.reportees.append(emp)

    def remove_reportee(self, emp):
        if emp in self.reportees:
            self.reportees.remove(emp)

    def print_emps(self):
        print(f'Manager, {self.fullname()}({self.alias}) has below reportees:')
        print()
        for emp in self.reportees:
            print(f' --> {emp.fullname()}')


# Below statements are to test different functionalities:

mgr_1 = Manager('steve', 'rogers', 90000)

emp_1 = Developer('clark', 'kent', 50000, 'python')
emp_2 = Developer('tony', 'stark', 60000, 'Java')
emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-50000'
emp_str_3 = 'peter-parker-30000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)

mgr_1.add_reportee(emp_1)
mgr_1.add_reportee(emp_2)
mgr_1.remove_reportee(emp_2)


# Print emp_1 object without __repr__ method
# (!) print(emp_1)
# <__main__.Developer object at 0x101c2f7d0>

# Print emp_1 object after defining __repr__ method above
# (!) print(emp_1)
# Employee: Clark Kent
#           alias: aclaken
#           email: clark.kent@acompany.com


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.language)
# print(mgr_1.email)
# mgr_1.print_emps()


# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_workday(my_date))

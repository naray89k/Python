#! /usr/bin/python
import datetime

class Employee(object):
    num_of_emps = 0
    raise_amount = 1.04
    #constructor
    def __init__(self,first,second,pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = '{}.{}@company.com'.format(self.first.lower(),self.second.lower())
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.second)

    def raise_pay(self):
        self.pay=self.pay*self.raise_amount

    @classmethod
    def set_raise_amt(empCls,amount):
        empCls.raise_amount = amount

    @classmethod
    def from_string(empCls,emp_str):
        frst,scnd,pay=emp_str.split('-')
        print frst,scnd,pay
        return empCls(frst,scnd,int(pay))

    @staticmethod
    def is_weekday(day):
        if day.weekday in [5,6]:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.second,self.pay)

    def __str__(self):
        return "{} -- {}".format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


#==== MAIN =====
emp_1 = Employee('Narayanan','Krishnan',50000)
emp_2 = Employee.from_string('Indhumathi-GopalaKrishnan-60000')

print emp_1
print emp_2


print emp_1.__repr__()
print emp_1.__str__()
print emp_2.__repr__()
print emp_2.__str__()

print emp_1 + emp_2
print len(emp_1)
print len(emp_2)


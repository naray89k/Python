#! /usr/bin/python

class Employee(object):

    #constructor
    def __init__(self,first,second,pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = '{}.{}@company.com'.format(self.first.lower(),self.second.lower())

    def fullname(self):
        return '{} {}'.format(self.first,self.second)

    def raise_pay(self,inc_percent):
        self.pay=self.pay*inc_percent

#class Employee Ends Here


emp_1 = Employee('Narayanan','Krishnan',50000)
emp_2 = Employee('Indhumathi','Gopal',60000)


# ANOTHE IMPORTANT THING TO KNOW:
# ==================================
# Why we are passing self object in all the functions. 
# The Below two statement works exactly the same way
emp_2.raise_pay(1.10)
Employee.raise_pay(emp_1,1.04)


print Employee.fullname(emp_2)
print emp_1.fullname()


print emp_1.__dict__
print emp_2.__dict__


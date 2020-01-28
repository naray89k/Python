#! /usr/bin/python

#class Employee Starts Here
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

#class Employee Ends Here

emp_1 = Employee('Narayanan','Krishnan',50000)
emp_1.raise_pay()
print emp_1.raise_amount
print emp_1.__dict__

emp_2 = Employee('Indhumathi','Gopal',60000)
emp_2.raise_amount=1.10
emp_2.raise_pay()
print emp_2.raise_amount
print emp_2.__dict__

# =========================
# Whats the take away from this Code.
# When 'raise_amount' is available in the instance namespace scope, Then it will be used in the function 'raise_pay'
# If that is not available, then 'raise_amount' in Class Variable will be used, In case that is not available in Class Scope.
# Then it will be checked in its Parents Classes one by One, all the way till Object Class.

#! /usr/bin/python
import re

class Employee(object):

    #constructor
    def __init__(self,first,second,pay):
        self.first = first
        self.second = second
        self.pay = pay


    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first.lower(),self.second.lower())


    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.second)


    @fullname.setter
    def fullname(self,name):
        self.first,self.second=name.split(' ')


    @fullname.deleter
    def fullname(self):
        self.first = None
        self.second = None
        self.pay = 0

    @email.setter
    def email(self,mailID):
        self.first,self.second = re.sub('@.*$','',mailID).split('.')

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.second,self.pay)


#class Employee Ends Here


emp_1 = Employee('Narayanan','Krishnan',50000)
emp_2 = Employee('Indhumathi','Gopal',60000)


print emp_1
emp_1.second='K'
print emp_1

emp_1.fullname = "Arulmozhi Thevan"
print emp_1

emp_2.email = "Amit.Gupta@company.com"
print emp_2
del emp_2.fullname
print emp_2


# What to take away from this video.
#   1.  @property makes the attributes email,fullname changed whenever the first & second is changed
#       But this will allow us to change the fullname or email later.
#   2.  @<property name>.setter makes 
#
# 


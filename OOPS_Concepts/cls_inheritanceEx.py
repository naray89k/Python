#! /usr/bin/python
import datetime

#class Employee starts here
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
        return empCls(frst,scnd,pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday in [5,6]:
            return False
        return True
#class Employee ends here

# =========================================================================================================================
# class Developer starts here
class Developer(Employee):
    raise_amount = 1.10
    no_of_dvlpr = 0

    def __init__(self,first,second,pay,prog_lang):
        super(Developer,self).__init__(first,second,pay)
        self.prog_lang=prog_lang
        Developer.no_of_dvlpr += 1
# class Developer ends here

# =========================================================================================================================
# class Manager starts here
class Manager(Employee):
    raise_amount = 1.10
    no_of_mgr = 0
    def __init__(self,first,second,pay,employees=None):
        super(Manager,self).__init__(first,second,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        Manager.no_of_mgr += 1

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print emp

# class Manager ends here
# =========================================================================================================================

#==== MAIN =====
emp_1 = Employee('Narayanan','Krishnan',50000)
#emp_2 = Employee('Indhumathi','Gopal',60000)
dev_1 = Developer('Indhumathi','Gopal',60000,['Java','C++'])
dev_2 = Developer('Narayanan','K',60000,['Java','Python'])
mgr_1 = Manager('Prabhakaran','Nalliah',90000,[dev_1])
print mgr_1.__dict__
mgr_1.add_emp(dev_2)
print mgr_1.__dict__
mgr_1.remove_emp(dev_1)
print mgr_1.__dict__
mgr_1.print_emps()

print dir(mgr_1)

print "==============================================="

print dir(emp_1)
#print dev_1.__dict__
#print dev_1.raise_pay()
#print dev_1.pay

#print help(Developer)



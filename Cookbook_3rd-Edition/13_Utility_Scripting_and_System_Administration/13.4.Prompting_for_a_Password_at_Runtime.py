#!/usr/bin/env python
# coding: utf-8
import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd): # You must write svc_login()
    print('Yay!')
else:
    print('Boo!')

user = input('Enter your username: ')


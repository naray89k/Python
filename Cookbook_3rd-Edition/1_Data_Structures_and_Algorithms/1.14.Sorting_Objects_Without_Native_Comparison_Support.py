#!/usr/bin/env python
# coding: utf-8
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __rep__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print users
print sorted(users)

from operator import attrgetter
sorted(users, key=attrgetter('user_id'))

by_name = sorted(users, key=attrgetter('user_id'))
by_name

print min(users, key=attrgetter('user_id'))
print max(users, key=attrgetter('user_id'))




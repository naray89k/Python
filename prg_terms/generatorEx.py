#! /usr/bin/python

#def square_numbers(nums):
#    for i in nums:
#        yield (i*i)
#
#my_nums=square_numbers([1,2,3,4,5])
#
#for num in my_nums:
#    print num

# ======= PRACTICAL EXAMPLE ========== #

import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print('Memory (Before): {}Mb '.format(mem_profile.memory_usage_psutil()))
print 'Memory (Before): {} MB'.format(str(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

#t1 = time.clock()
#people = people_generator(1000000)
#t2 = time.clock()

#print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print 'Memory (After) : {} MB'.format(str(mem_profile.memory_usage()))

print 'Took {} Seconds'.format(t2-t1)
#print ('Took ' + str(t2-t1) + ' Seconds')

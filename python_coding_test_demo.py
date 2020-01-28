#! /usr/bin/env python



# This is a demo task.
# Write a function:
#     def solution(A)
# 
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    negative_less_array = [ elem for elem in A if elem > 0 ]
    start = 1
    largest = max(negative_less_array, default=0)
    result = 1
    if largest < 1:
        return result
    for elem in range(start, (largest + 1)):
        if elem in negative_less_array:
            result += 1
            continue
        else:
            return elem
    return result

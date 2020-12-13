#! /usr/bin/env python3

from math import sqrt


# This Example best demonstrate the usage of filter function

def is_prime(num):
    """ This function checks whether given number is prime or not """
    if num == 1:
        return True
    else:
        for elem in range(2, (int(sqrt(num)) + 1)):
            if num % elem == 0:
                return False
        return True


# = = = MAIN = = =
if __name__ == '__main__':
    prime_numbers_with_in_thousand = list(filter(is_prime, list(range(1, 1001))))
    print("List of prime numbers between 1 to 1000")
    for elem in prime_numbers_with_in_thousand:
        print(elem)

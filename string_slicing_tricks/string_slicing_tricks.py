#! /usr/bin/env python3

# Example-1:
print('Example-1')
word = 'tacocat'
subword = word[0:3]  # --> Say Hello! to slicing operator.
print(word, subword)
print('')

# Example-2:
print('Example-2')
subword = word[:]  # --> creates a copy of the string.
# --> Address location of the copy of the string same as
# tacocat
print(word, subword)
print('')

# Example-3:
print('Example-3')
word = "tacocat"
character = word[-3]  # ---> Third character counting from the end.
# ---> Last character of a string is access with [-1].
# character = c
print(word, character)

subword = word[-3:]  # ---> From third last to the end.
# cat
print(word, subword)
print('')

# Example-4:
# string[start:stop:step]
print('Example-4')
word = "tacocat"
subword = word[::2]  # ---> From start (0) to end, take every second character!.
print(word, subword)
# tcct
other = word[1::2]  # ---> Starting with the second character, take every second character!.
print(word, other)
# aoa
print('')

# Example-5:
print('Example-5')
word = "taco"
subword = word[::-1]  # ---> want to reverse a string ?. Do it like this!.
# ocat
print(word, subword)

other = word[::-2]
# oa.
print(word, other)
print('')

# Example-6:
print('Example-6')
print('Polyndrome check')
word = "madam"
print('Is this a Polyndrome string ?.', word == word[::-1])

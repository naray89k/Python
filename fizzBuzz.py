#! /bin/python3

def fizzBuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def get_first_char(chars_pos_dict):
    first_pos = min([pos for pos in chars_pos_dict.values()])
    for char, pos in chars_pos_dict.items():
        if pos == first_pos:
            return char


def maximumOccurringCharacter(text):
    chars_set = {c for c in text}
    chars_count_dict = {c: text.count(c) for c in chars_set}
    max_occurrence = max([count for count in chars_count_dict.values()])
    max_chars = [char for char, count in chars_count_dict.items() if count == max_occurrence]
    chars_position_dict = {char: text.find(char) for char in max_chars}
    return get_first_char(chars_position_dict)


# ============================================ REFINED ========================================================

def get_first_max_occuring_char(chars_pos_dict, max_occurence, min_index):
    for char, details in chars_pos_dict.items():
        if details[0] == max_occurence and details[1] == min_index:
            return char
    return ''


def maximumOccurringCharacter(text):
    chars_count_dict = {c: [text.count(c), text.find(c)] for c in text}
    max_occurrence = max([details[0] for c, details in chars_count_dict.items()])
    min_index_max_chars = min([details[1] for c, details in chars_count_dict.items() if max_occurrence == details[0]])
    return get_first_max_occuring_char(chars_count_dict, max_occurrence, min_index_max_chars)


# ============================================ REFINED ========================================================

#def get_anagrams(string1, strings_list):
#    anagram_list = []
#    for string in strings_list:
#        if string1 != string:
#            if sorted(string1) == sorted(string):
#                anagram_list.append(string)
#    print(anagram_list)
#    return anagram_list
#
#
#def anagram_check(string1, strings_list):
#    for string in strings_list:
#        if string1 != string:
#            if sorted(string1) == sorted(string):
#                return True
#    return False
#
#
#def funWithAnagrams(text):
#    temp_string_list = []
#    for elem in text:
#        anagrams = get_anagrams(elem, text)
#        if anagrams:
#            if not anagram_check(elem, temp_string_list):
#                temp_string_list.append(elem)
#        else:
#            temp_string_list.append(elem)
#    print(sorted(temp_string_list))

# ============================================ REFINED ========================================================

def anagram_check(string1, strings_list):
    for string in strings_list:
        if (string1 == string) or (sorted(string1) == sorted(string)):
            return True
    return False


def funWithAnagrams(text):
    temp_string_list = []
    for elem in text:
        if anagram_check(elem, temp_string_list):
            continue
        else:
            temp_string_list.append(elem)
    return sorted(temp_string_list)
# ============================================ REFINED ========================================================

# Write your code here


if __name__ == '__main__':
    # num_range = 15
    # fizzBuzz(num_range)
    maximumOccurringCharacter("NARAYANAN * $")
    input_list = ['code', 'doce', 'ecod', 'framer', 'frame']
    print(funWithAnagrams(input_list))

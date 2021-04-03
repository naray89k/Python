#! /usr/bin/env python


# ================================ Data types =================================
# List

# ===============================================================================
# Dictionaries
# ===============================================================================
# country_capital = {"India": "delhi",
#                   "USA": "Washington",
#                   "UK": "London",
#                   "India": "Chennai"
#                   }
# print(country_capital)
# country_capital["USA"] = "San Francisco"
# country_capital["Germany"] = "Berlin"
# country_capital["France"] = "Paris"
# print(country_capital)
# print(country_capital.keys())
# country_capital = {}

# ===================================================================
# Set
# ===================================================================
# countries = {"India", "France", "USA", "UK", "Germany"}
# developed_countries = {"USA", "UK", "Canada", "Australia", "Germany"}
# print(developed_countries.union(countries))
# print(developed_countries.difference(countries))
# print(sorted(countries))
#
# for elem in dir(countries):
#    if not elem.endswith('__'):
#        print(elem)
#
# ===================================================================
# tuple
# ===================================================================
single_element_tuple = "number_one",
print(type(single_element_tuple))
multiple_element_tuple = (1, 2, 3, 5, 7)
print(multiple_element_tuple[2:])

# Trick
list1 = list(range(1, 11))
list2 = list(range(11, 21))
print(list1, list2)
multiple_element_tuple_2 = (list1, list2)
print(multiple_element_tuple_2)

list1.append(11)
list2.append(21)
print(multiple_element_tuple_2)

# ================================ Conditional Loops ==========================


# ================================ for loop ==========================


# ================================ while Loop ==========================


# ================================ Functions ==========================

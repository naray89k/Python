#! /usr/bin/env python3

import csv

city_distances_in_km = [('Birmingham', 162),
                        ('Liverpool', 286),
                        ('Nottingham', 175),
                        ('Sheffield', 227),
                        ('Bristol', 171),
                        ('Glasgow', 555),
                        ('Leicester', 143),
                        ('Edinburgh', 533),
                        ('Leeds', 272),
                        ('Cardiff', 211),
                        ('Manchester', 261),
                        ('Stoke-on-Trent', 217),
                        ('Coventry', 138),
                        ('Sunderland', 386),
                        ('Birkenhead', 286),
                        ('Islington', 3),
                        ('Reading', 59),
                        ('Kingston upon Hull', 249),
                        ('Preston', 305),
                        ('Newport', 199)]

km_to_mi = lambda data: (data[0], round(0.621371192 * data[1], 1))
city_distances_in_miles = list(map(km_to_mi, city_distances_in_km))
# print(city_distances_in_miles)

with open('distance_chart.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['S.No', 'CITY', 'FROM LONDON (Km)', 'FROM LONDON (Mi)'])
    count = 1
    for tuple_1, tuple_2 in zip(city_distances_in_km, city_distances_in_miles):
        print(count, tuple_1[0], tuple_1[1], tuple_2[1])
        csv_writer.writerow([count, tuple_1[0], tuple_1[1], tuple_2[1]])
        count += 1

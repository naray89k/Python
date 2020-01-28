#! /usr/bin/env python3

import lxml.etree as ET
import csv

xml_file="books.xml"
tree = ET.parse(xml_file)

with open('books_detail.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['S.No','AUTHOR','TITLE','GENRE','PRICE'])
    count = 1
    for elem in tree.xpath('.//book'):
        author = elem.find('author').text
        title = elem.find('title').text
        genre = elem.find('genre').text
        price = elem.find('price').text
        row = [count, title, author, genre, price]
        csv_writer.writerow(row)
        count += 1


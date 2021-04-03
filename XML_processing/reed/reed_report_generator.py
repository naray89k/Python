#! /usr/bin/env python3

import lxml.etree as ET
import csv

xml_file = "reed.xml"
tree = ET.parse(xml_file)

with open('reed.csv', 'w') as csvfile:
    # fieldnames = ['Registration No', 'Title', 'Subj', 'Instructor']
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Registration No', 'Title', 'Subj', 'Instructor'])
    for elem in tree.xpath('.//course'):
        row = [elem.find("reg_num").text,
               elem.find("title").text,
               elem.find("subj").text,
               elem.find("instructor").text]
        csv_writer.writerow(row)

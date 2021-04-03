#! /usr/bin/env python3

import lxml.etree as ET
import xml.etree.cElementTree as html_tree
import xml.dom.minidom as mnDom

from lxml.html import builder as E
import csv

xml_file = "resume.xml"
tree = ET.parse(xml_file)
table_header = ['S.No', 'CLIENT', 'START_DATE', 'END_DATE', 'ROLE', 'TYPE', 'LOCATION']
table_data = []

with open('project_assignments.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(table_header)
    count = 1
    for elem in tree.xpath('.//project'):
        client_tag = elem.find('client')
        client_name = client_tag.attrib['name']
        location = client_tag.attrib['location']
        position_tag = elem.find('position')
        role = position_tag.attrib['title']
        role_type = position_tag.attrib['type']
        start_date = elem.attrib['start']
        end_date = elem.attrib['end']
        row = [count, client_name, start_date, end_date, role, role_type, location]
        table_data.append([count, client_name, start_date, end_date, role, role_type, location])
        csv_writer.writerow(row)
        count += 1

# HTML TAG CREATION:
root_elem = html_tree.Element('html')
hdElem = html_tree.SubElement(root_elem, 'head')
html_tree.SubElement(hdElem, 'h2').text = "List of Job Assignments"
body_elem = html_tree.SubElement(root_elem, 'body')

table_elem = html_tree.SubElement(body_elem, 'table', border='1')
table_row_elem = html_tree.SubElement(table_elem, 'tr')
for th in table_header:
    html_tree.SubElement(table_row_elem, 'th').text = th

for row in table_data:
    table_row_elem = html_tree.SubElement(table_elem, 'tr')
    for col in row:
        html_tree.SubElement(table_row_elem, 'td').text = str(col)

rough_string = html_tree.tostring(root_elem)
reparsed = mnDom.parseString(rough_string)
filename = "project_assignments.html"
FILE = open(filename, "w")
FILE.writelines(reparsed.toprettyxml(indent="\t"))
FILE.close()

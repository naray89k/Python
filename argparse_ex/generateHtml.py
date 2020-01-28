#! /usr/bin/env python3

import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys


htmlStr="""<!DOCTYPE html>
<html>
  <body>
    <p>
    <br/>
    </p>
  </body>
  <h3><font color='green'><b>RANGE {rnge}</b></font></h3>
  <h4><font color='blue'><b>SQUARES AND CUBE TABLE</b></font></h4>
  {TABLE1}
  <br/>
  <h3><font color="red"><b>SUM ON INTEGERS TABLE</b></font></h3>
  {TABLE2}
  <hr>
</html>"""


def parseArgs():
    parser = argparse.ArgumentParser(description='The Script generates the Square,Cube,Sum of Numbers in html format')
    parser.add_argument("-r","--range",type=int,required=True,help="Range in Integer")
    return parser.parse_args()

def genSqrCubTable(rnge):
    tableStr='<table border = "1" bordercolor="#696969">\n \
            <tr><th>N</th><th>SQUARE OF N</th><th>CUBE OF N</th>\n'
    for i in range(1,(rnge+1)):
        tableStr=tableStr+"\t"+"<tr><td>{}</td><td bgcolor=\"#9ACD32\">{}</td><td bgcolor=\"#FA8072\">{}</td></tr>\n".format(i,pow(i,2),pow(i,3))
    tableStr=tableStr+"</table>"
    return tableStr


def genSumOfNumbers(rnge):
    tableStr='<table border = "1" bordercolor="#696969">\n \
            <tr><th>N</th><th>SUM ON N Numbers</th>\n'
    for i in range(1,(rnge+1)):
        tableStr=tableStr+"\t"+"<tr><td>{}</td><td>{}</td></tr>\n".format(i,(i*(i+1))/2)
    tableStr=tableStr+"</table>"
    return tableStr


#MAIN
args=parseArgs()
#print args
table1=genSqrCubTable(args.range)
table2=genSumOfNumbers(args.range)

htmlStr=htmlStr.format(rnge=args.range,TABLE1=table1,TABLE2=table2)

fileObj=open("table.html",'w')
fileObj.write(htmlStr)
fileObj.close()


# Create message container - the correct MIME type is multipart/alternative.
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "TEST MAIL"
# msg['From'] = 'narayanan.k.1985@gmail.com'
# msg['To'] = 'narayanan.k.1985@gmail.com'
# HTML_BODY = MIMEText(htmlStr, 'html')
# msg.attach(HTML_BODY)
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login('narayanan.k.1985@gmail.com','***********')
# server.sendmail('narayanan.k.1985@gmail.com',['narayanan.k.1985@gmail.com'],msg.as_string())
# server.quit()

#!/usr/bin/env python
# coding: utf-8
import ipaddress
net = ipaddress.ip_network('123.45.67.64')
net

for a in net:
    print(a)

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
net6

for a in net6:
    print(a)

net.num_addresses
net[0]

net[1]

net[-1]

net[-2]

a = ipaddress.ip_address('123.45.67.69')
a in net

b = ipaddress.ip_address('123.45.67.123')
b in net

inet = ipaddress.ip_interface('123.45.67.73/27')
inet.network

inet.ip

a = ipaddress.ip_address('127.0.0.1')
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect((a, 8080))

s.connect((str(a), 8080))


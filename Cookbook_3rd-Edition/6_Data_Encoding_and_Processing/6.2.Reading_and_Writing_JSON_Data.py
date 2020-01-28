#!/usr/bin/env python
# coding: utf-8
import json

data = {
 'name' : 'ACME',
 'shares' : 100,
 'price' : 542.23
}

json_str = json.dumps(data)

data = json.loads(json_str)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
    
    
# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

json.dumps(False)

d = {'a': True,
     'b': 'Hello',
     'c': None}

json.dumps(d)

# Python 3

from urllib.request import urlopen
from pprint import pprint

import json
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
data

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
data.name

data.shares

data.price

print(json.dumps(data))

print(json.dumps(data, indent=4))

print(json.dumps(data, sort_keys=True))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
json.dumps(p)

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
classes = {
 'Point' : Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
s

a = json.loads(s, object_hook=unserialize_object)
a

a.x

a.y


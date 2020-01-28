#!/usr/bin/env python
# coding: utf-8
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
 
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
 
    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()
 
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)

del root
print(c1.parent)

# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

a = Data()
del a 

a = Node()
del a 

a = Node()
a.add_child(Node())
del a 

import gc
gc.collect() 

# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
 # NEVER DEFINE LIKE THIS.

 # Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del.parent
        del.children
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

a = Node()
a.add_child(Node()
del a # No message (not collected)
import gc
gc.collect() # No message (not collected)

import weakref
a = Node()
a_ref = weakref.ref(a)
a_ref

print(a_ref())

del a

print(a_ref())


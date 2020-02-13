#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:03:22 2020

@author: iris
"""

a = "Hello World!!!"
b = a[0:5]
print(b)
c = a[6:11]
print(c)
d = a[11:14]
print(d)

flag = "ello" in a
#print(flag)
if flag == True:
    print("ello is in a")
else:
    print("ello is not in a")
    
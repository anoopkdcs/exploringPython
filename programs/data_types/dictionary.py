#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:58:23 2017

@author: manjary
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
print("\n %s is %d years" %(dict['Name'], dict['Age']))

del dict['Name']
print(dict)

dict.clear()
print(dict)


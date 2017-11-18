#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:41:14 2017

@author: manjary
"""

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

membership1 = 'physics' in list1
membership2 = 'physics' in list2
membership3 = 'physics' not in list2

print("membership of physics in list1 =", membership1)
print("membership of physics in list2 =", membership2)
print("membership of physics not in list2 =", membership3)
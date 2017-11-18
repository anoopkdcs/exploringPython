#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:15:58 2017

@author: manjary
"""

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print(list1[0])
print(list1[2])
print(list1[1:3])
print(list2[1])
print(list3[2])

l1 = len(list1) 
l2 = len(list2) 
print("length of list1 = %d, length of list2 = %d" %(l1,l2))

print(list2)
list2[2] = 100
print(list2)


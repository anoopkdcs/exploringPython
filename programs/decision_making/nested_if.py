#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:11:07 2017

@author: manjary
"""

var = int(input("enter a number"))
if var < 200:
   print("Expression value is less than 200")
   if var == 150:
      print("The value is 150")
   elif var == 100:
      print("The value is 100")
   elif var == 50:
      print("The value is 50")
elif var < 50:
   print("Expression value is less than 50")
else:
   print("Good bye!")
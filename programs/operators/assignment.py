#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:14:25 2017

@author: manjary
"""

a = 10
b = 20

c = a + b
print("a + b =", c)

c **= a
print("c = c  ** a gives", c )

c //= a
print("c = c  // a gives", c )

c = a + b

c += a
print("c = c  + a gives", c )

c -= a
print("c = c  - a gives", c )

c *= a
print("c = c  * a gives", c )

c /= a
print("c = c  / a gives", c )

c %= a
print("c = c  % a gives", c )
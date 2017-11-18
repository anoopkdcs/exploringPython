#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:21:45 2017

@author: anoop
"""

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data="artificial intelligence is my favorite subject. I am also love machine learning"
words=word_tokenize(data)

#defining stopwords
stop_words=set(stopwords.words("english"))

stop_words.add("is")

#filtering 
filterData=[]
for w in words:
    if w not in stop_words:
        filterData.append(w)
        
        
        

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:29:30 2017

@author: anoop
"""
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

data="artificial intelligence is my favorite subject. I am also love machine learning"

token1=sent_tokenize(data)
token2=word_tokenize(data)

for word in token2:
    print word
    
for sent in token1:
    print sent






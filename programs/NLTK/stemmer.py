#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:36:56 2017

@author: anoop
"""

from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.tokenize import word_tokenize

#example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
word="cacti"

ps=PorterStemmer()
stemmedData1=ps.stem(word)


ss=SnowballStemmer("english", ignore_stopwords="True")
stemmedData2=ss.stem(word)



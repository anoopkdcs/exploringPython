#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:47:49 2017

@author: anoop


Note:cacti:a succulent plant with a thick fleshy stem which typically bears spines, lacks leaves, and has brilliantly coloured flowers. Cacti are native to arid regions of the New World and are cultivated elsewhere, especially as pot plants.
"""
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer

#example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
word="pythoner"
lemmatizer = WordNetLemmatizer()

lematizedWord=lemmatizer.lemmatize(word)



print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))


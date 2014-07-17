#!/usr/bin/env python

#
# NOTE OK, here's the plan, we'll 'tag' the keywords and use tag frequencies to form clusters
#
# Specifically, form a similarity matrix on all the tags with (i,j) = frequency of (i,j)/frequency of (i)
# we'll then use same-size k-means variation to get clusters of 30 keywords
#
# It probably would have been a good idea to do this (as a prototype) in Matlab but that's life...
# After prototyping we'd work this into actual development code (viz. in Scala)
#

from nltk import *
import re

file_name = "IV6 - RAW keywords.txt"
with open(file_name) as f:
    text = f.readlines()

#
# tokenize all words 

words = tokenize.word_tokenize("".join(text))

#
# filter out stop words (apparently there aren't any)
stop = set(corpus.stopwords.words('english'))
stopless = filter(lambda w: not w in stop,words)

#
# now use stemmer to remove plurals

stemmer = stem.porter.PorterStemmer()
singles = []
for word in stopless:
    singles.append(stemmer.stem(word))

# generate frequency distribution on clean tags 
fdist = FreqDist(singles)

# get tags (we'll only use 300 since the tag frequencies fall off fast)
tags = fdist.keys()[:300]


#
# generate similarity matrix 

# compute frequency of (i,j) 

# need to clean up the individual lines (could have initially done this on a line by line basis)
clean_text = []
for line in text:
    words_ = tokenize.word_tokenize(line)
    stopless_ = filter(lambda w: not w in stop,words_)
    singles_ = []
    for word_ in stopless_:
        singles_.append(stemmer.stem(word_))
    clean_text.append(" ".join(singles_))
print len(clean_text)


# (i,j) = frequency of (i,j)/frequency of (i)
matrix = {}
#for i, tagi in enumerate(tags):
#    matrix[i] = {}
#    for j, tagj in enumerate(tags):
#        matrix[i][j] = 

#
# same-size k-means variation

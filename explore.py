#!/usr/bin/env python

# *******************************************
# Problem Description
# *******************************************
# Given the file of keywords (each row is a keyword, even if it contains more than one individual word), 
# write a program to group these keywords into clusters of approximately 30 semantically relevant keywords 
# (each cluster does not have to contain exactly 30 keywords). You can write the code in any language that 
# you are comfortable with. Please include the resulting clusters in your submission.
# *******************************************

# NOTE this file is for exploratory work


# NOTE We'll use NLTK for exploration and possibly for data clustering
from nltk import *

import re


# NOTE must get resources in python console first using:
#nltk.download()

#
# Import 

# NOTE the words appear to be all lower case and only nouns
#      and there are 50000 keywords (=> 1666 clusters)
#      looking at the corpus it seems to be entirely about post secondary education (the below analyses confirm this)
file_name = "IV6 - RAW keywords.txt"

with open(file_name) as f:
    text = f.readlines()

#
# tokenize all words (not just clusters)

words = tokenize.word_tokenize(text)
fdist = FreqDist(words)

# NOTE total number and unique words
print fdist.N(), fdist.B()
# -> 191180
# -> 7186


#
# filter out stop words (apparently there aren't any)
stop = set(corpus.stopwords.words('english'))
stopless = filter(lambda w: not w in stop,words)

fdist = FreqDist(stopless)

print fdist.N(), fdist.B()
# -> 171684
# -> 7116


#
# now use stemmer to remove plurals

stemmer = stem.porter.PorterStemmer()
singles = []
for word in stopless:
    singles.append(stemmer.stem(word))

fdist = FreqDist(singles)

print fdist.N(), fdist.B()
# -> 171684
# -> 6246

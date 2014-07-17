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

#stemmer = stem.porter.PorterStemmer()


# NOTE
# I was trying to exhaustively tag the keywords conceptually (based on state, region, &c) which would maybe be good for an online
# algorithm but I'll be easier to simply use the most frequent words as tags

##
## generate lists of geographical info for tagging
#
#states = {}
#states_abbr = {}
#with open("states.csv") as f:
#    for line in f:
#        m = re.match(r'"(.+)","(\w+)"', line)
#        states[m.group(1).lower()] = m.group(2).lower()
#        states_abbr[m.group(2).lower()] = m.group(2).lower()
#
##for key, val in states.iteritems():
##    print "%s %s" % (key, val)
#
## tag states
#tagged_lines = {}
#for ind, line in enumerate(text):
#    for key, val in states.iteritems():
#        if key in line:
#            tagged_lines[ind] = [val]
#    for key, val in states_abbr.iteritems():
#        if key in line.split():
#            tagged_lines[ind] = [val]
#
#print len(tagged_lines)
## -> 22999
#
##
## NOTE it'd be nice to tag cities but we don't have time to create a list...
#
#
##
## tag types of schools: university, college, school
#schools = ["college", "university", "school", "online", "community", "

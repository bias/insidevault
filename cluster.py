#
# NOTE OK, here's the plan, we'll 'tag' the keywords and use tag frequencies to form clusters
#

from nltk import *
import re

file_name = "IV6 - RAW keywords.txt"

#
# generate lists of geographical info for tagging

states = {}
with open("states.csv") as f:
    for line in f:
        m = re.match(r'"(\w+)","(\w+)"', line)
        states[m.group(1)] = m.group(2)
        states[m.group(2)] = m.group(2)

for line in text:
    for state in
    if re.match(

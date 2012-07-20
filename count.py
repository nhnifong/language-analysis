from __future__ import division
from glob import glob
from collections import defaultdict
import codecs

all_languages = {}

for filename in glob("natural/*.txt"):
    lang = filename[len('natural/'):-len('.txt')]
    stats = defaultdict(lambda: 0)
    text = codecs.open(filename, 'r', 'utf-8').read()
    # count characters
    for c in text:
        stats[c] += 1
    # normalize
    for key in stats.keys():
        stats[key] = stats[key] / len(text)
        
    all_languages[lang] = dict(stats)
    
# make sure every language has the same set of keys
allkeys = set()
for langdict in all_languages.values():
    allkeys = allkeys.union(langdict.keys())
for langdict in all_languages.values():
    for key in allkeys:
        if not langdict.has_key(key):
            langdict[key] = 0
    
outf = open('character_counts.py','w')
outf.write('all_languages = %r\n' % all_languages)
outf.close()

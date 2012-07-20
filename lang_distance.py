from __future__ import division
from character_counts import all_languages
from collections import defaultdict

def lang_distance(text):
    text = unicode(text)
    distrib = defaultdict(lambda: 0)
    # count chars
    for char in text:
        distrib[char] += 1
    # normalize
    for key in distrib.keys():
        distrib[key] = distrib[key] / len(text)
    
    keys = all_languages['english'].keys() # they all have the same set of keys, 'english' is an arbitrary way of fetching it
    
    result = {}
    
    for langname, lang in all_languages.items():
        # simple vector distance
        totald = 0.0
        for key in keys:
            totald += (lang[key] - distrib[key]) ** 2
        totald = totald ** 0.5
        result[langname] = totald
    
    # nice table of language distances
    maxnamelen = max(map(len,result.keys()))
    res = sorted(result.items(), key=lambda x: x[1], reverse=True)
    for langname,val in res:
        print langname + (' '*(3+maxnamelen-len(langname))) + str(val)

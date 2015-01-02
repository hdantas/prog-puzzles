# http://www.codewars.com/kata/53e895e28f9e66a56900011a

import re

def letter_frequency(text):
    text = sorted(re.sub("[^a-z]",'',text.lower()))
    result = []
    index = 0
    while index < len(text):
        t = text[index]
        count = text.count(t)
        result += [(t, count)]
        index += count
    
    return sorted(result, key=lambda tup: tup[1], reverse = True)
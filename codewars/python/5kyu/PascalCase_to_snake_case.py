# http://www.codewars.com/kata/529b418d533b76924600085d

def to_underscore(string):
    if not isinstance(string, basestring): return str(string)
    return string[0].lower() + ''.join(["_" + c.lower() if c.isupper() else c for c in string[1:]])
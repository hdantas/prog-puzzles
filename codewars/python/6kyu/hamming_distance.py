# http://www.codewars.com/kata/5410c0e6a0e736cf5b000e69

def hamming(a,b):
    return sum([c1 != c2 for c1, c2 in zip(a,b)])
# http://www.codewars.com/kata/52f787eb172a8b4ae1000a34
import math

def zeros(n):
    return sum([n / (5 ** x) for x in range(1, int(math.log(n,5)) + 1)]) if n else 0

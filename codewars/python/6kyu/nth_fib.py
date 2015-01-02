# http://www.codewars.com/kata/522551eee9abb932420004a0

def nth_fib(n):
    result = 0
    a = 0
    b = 1
    for i in xrange(1, n):
        a = b
        b = result
        result = a + b
    
    return result
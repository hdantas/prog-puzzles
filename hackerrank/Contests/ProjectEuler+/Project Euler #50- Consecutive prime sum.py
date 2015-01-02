import math
import random


def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)

    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def sumPrimes(prime_list):
    new_list = [0] * (len(prime_list) + 1)
    for i in range(len(prime_list)):
        new_list[i + 1] = new_list[i] + prime_list[i]

    return new_list

 
def rabinMiller(num):
    # Returns True if num is a prime number.
 
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    
    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)

def do_work(n, prime_list, sum_list):
    # print "len", len(prime_list)
    # print "prime_list", prime_list

    tmp_sum = prime_list[0]
    old_sum = tmp_sum
    delta_estimate = int(math.ceil(n ** 0.5) / 3)
    tmp_list = [0, delta_estimate]

    min_index = 0
    max_index = min_index + tmp_list[1]

    # while sum(prime_list[min_index:max_index + 1]) <= n and max_index < len(prime_list):
    while (sum_list[max_index + 1] - sum_list[min_index]) <= n and max_index < len(prime_list):
        while tmp_sum <= n and max_index < len(prime_list):
            # tmp_sum = sum(prime_list[min_index:max_index + 1])
            tmp_sum = sum_list[max_index + 1] - sum_list[min_index]

            # print  "tmp_sum", tmp_sum, "\tmin_index", min_index, "\tmax_index", max_index, "\tdelta", max_index - min_index + 1

            if isPrime(tmp_sum):
                delta = max_index - min_index + 1
                if delta > tmp_list[1] and tmp_sum <= n:
                    tmp_list = [tmp_sum, delta]
                    # print "\ttmp_list", tmp_list

            max_index += 1
        
        min_index += 1
        max_index = min_index + tmp_list[1]
        tmp_sum = prime_list[min_index]
    

    return str(tmp_list[0]) + " " + str(tmp_list[1])

# Enter your code here. Read input from STDIN. Print output to STDOUT

# val = [10 ** 5, 20 ** 6, 4 ** 9, 10 ** 10, 50 * 6, 80 * 2, 10 * 4]
# n = len(val)
val = []
n = int(raw_input())
for i in range(n):
    val.append(int(raw_input()))


prime_list = primes2(int(math.ceil(max(val) ** 0.5)) * 10)
sum_list  = sumPrimes(prime_list)

s = list(set(val))
result = {}
for i in range(len(s)):

    tmp = do_work(s[i], prime_list, sum_list)
    result[s[i]] = tmp

for i in range(n):
    print result[val[i]]





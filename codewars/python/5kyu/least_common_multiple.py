# http://www.codewars.com/kata/5259acb16021e9d8a60010af

from fractions import gcd

def lcm(*args):
  return reduce(lambda x,y : x * y / gcd(x,y), args)

print lcm(4, 10) == 20
print lcm(2,5) == 10
print lcm(2,3,4) == 12
print lcm(9) == 9
print lcm(0) == 0
print lcm(0,1) == 0
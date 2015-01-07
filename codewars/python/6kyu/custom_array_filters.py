# http://www.codewars.com/kata/53fc954904a45eda6b00097f/train/python

class list(list):
  def __init__(self, l): self.l = [x for x in l if isinstance(x, int)]
  def even(self): return [x for x in self.l if x % 2 == 0]
  def odd(self): return [x for x in self.l if x % 2 != 0]
  def under(self, val): return [x for x in self.l if x < val]
  def over(self, val): return [x for x in self.l if x > val]
  def in_range(self, low, high): return [x for x in self.l if low <= x <= high]

print list([1,2,3,4,5]).even() == [2,4]
print list([1,2,3,4,5]).odd() == [1,3,5]
print list([1,2,3,4,5]).under(4) == [1,2,3]
print list([1,2,3,4,5]).over(4) == [5]
print list([1,2,3,4,5]).in_range(1, 3) == [1,2,3]

print list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) == [2,4]
print list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() == [300, 122]

print list([1,2,3,4,5]).even() == [2,4]
print list([1,2,3,4,5]).odd() == [1,3,5]

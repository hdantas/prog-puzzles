# http://www.codewars.com/kata/53d2697b7152a5e13d000b82

import copy
def copy_list(l):
  if(l == None):
        raise
  return copy.copy(l)
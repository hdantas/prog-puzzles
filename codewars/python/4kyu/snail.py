# http://www.codewars.com/kata/snail

def snail(array):
    if not len(array): return []
    return array[0] + \
           [row[-1] for row in array[1:]] + \
           array[-1][-2::-1] + \
           [row[0] for row in array[-2:0:-1]] + \
           snail([row[1:-1] for row in array[1:-1]])


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print snail(array) == expected


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print snail(array) == expected

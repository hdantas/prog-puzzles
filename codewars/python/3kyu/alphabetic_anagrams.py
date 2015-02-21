# http://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python

# Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words"). For any word with at least two different letters, there are other words composed of the same letters but in a different order (for instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters as these two).

# We can then assign a number to every word, based on where it falls in an alphabetically sorted list of all words made up of the same set of letters. One way to do this would be to generate the entire list of words and find the desired one, but this would be slow if the word is long.

# Given a word, return its number. Your function should be able to accept any word 25 letters or less in length (possibly with some letters repeated), and take no more than 500 milliseconds to run. To compare, when the solution code runs the 27 test cases in JS, it takes 101ms.

# For very large words, you'll run into number precision issues in JS (if the word's position is greater than 2^53). For the JS tests with large positions, there's some leeway (.000000001%). If you feel like you're getting it right for the smaller ranks, and only failing by rounding on the larger, submit a couple more times and see if it takes it. If it's still a widespread problem, I'll add more leeway.

# Python, Java and Haskell have arbitrary integer precision, so you must be precise in those languages (unless someone corrects me).

# Sample words, with their rank:
# ABAB = 2
# AAAB = 1
# BAAA = 4
# QUESTION = 24572
# BOOKKEEPER = 10743

import math

def listPosition(word):
  """Return the anagram list position of the word"""
  if len(word) == 1:
    return 1

  unique_words = sorted(list(set(word))) # remove duplicates and sort it
  freq_letters = [word.count(letter) for letter in unique_words] # number of times each letter appears
  # Total number of possible combinations m!/(n! * (n-1)! * ...)
  total_combinations = math.factorial(len(word)) / reduce(lambda x,y: x * y, [math.factorial(freq) for freq in freq_letters])

  increment = [0] + [freq * total_combinations / len(word) for freq in freq_letters[:-1]]
  increment = [sum(increment[:i + 1]) for i in range(len(increment))]
  
  return increment[unique_words.index(word[0])] + listPosition(word[1:])


testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
for word in testValues:
  print "word", word, "\t rank:", listPosition(word)
  if not listPosition(word) == testValues[word]: print ('Incorrect list position for: ' + word) 



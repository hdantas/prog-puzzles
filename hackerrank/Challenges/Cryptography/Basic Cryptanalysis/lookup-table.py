import string
import json
# Just ignore the fact that it is english.
# The words are from the dictionary. So maybe you can preprocess dictionary and make a frequency table. 
# More over if you can narrow down one word with say 5 letter's you can remove candidates by trial and error on other words.

lookup = dict()

inputfile = open('dictionary.lst', 'r')
outputfile = open('lookup-table.txt', 'w')

for word in inputfile.readlines():
	word = word.replace('\n', '').lower()
	freq = []
	for letter in word:
		freq.append(round(float(word.count(letter)) / len(word), 4))
	
	print word + "\t", freq
	lookup[word] = freq


outputfile.write(json.dumps(lookup))

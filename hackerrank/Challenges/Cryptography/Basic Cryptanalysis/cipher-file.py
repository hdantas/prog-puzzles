import random

inputfile = open('newtestcase-decoded.txt', 'r')
outputfile = open('newtestcase-encoded.txt', 'w')

key = [chr(i + ord('a')) for i in range(26)]

random.shuffle(key)
# key = ['u', 'd', 'm', 'w', 'q', 'x', 'y', 'b', 'e', 'a', 'h', 'n', 'j', 'z', 'k', 'l', 'o', 'r', 'p', 'v', 't', 'f', 'c', 'i', 'g', 's']


words = inputfile.readline().split(' ')
newwords = [] #[''] * len(words)

for word in words:
	newword = ""
	for i in xrange(len(word)):
		letter = word[i]
		newword += key[ord(letter) - ord('a')]
	
	newwords.append(newword)

outputfile.write(' '.join(newwords))


inputfile.close()
outputfile.close()

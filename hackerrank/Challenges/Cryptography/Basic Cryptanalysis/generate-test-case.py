import random


MAXCHAR = 1000

inputfile = open('dictionary.lst', 'r')
outputfile = open('newtestcase-decoded.txt', 'w')

corpus = []

for word in inputfile.readlines():
	corpus.append(word.replace('\n', '').lower())


rand = random.random()
random.shuffle(corpus)
testcase = ""

cnt = 0
for word in corpus:
	testcase += word + " "
	cnt += len(word) + 1
	if cnt > MAXCHAR:
		break


outputfile.write(testcase[:-1])

inputfile.close()
outputfile.close()
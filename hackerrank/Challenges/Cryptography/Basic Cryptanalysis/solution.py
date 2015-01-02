import string
import time
import json
import re

# Just ignore the fact that it is english.
# The words are from the dictionary. So maybe you can preprocess dictionary and make a frequency table. 
# More over if you can narrow down one word with say 5 letter's you can remove candidates by trial and error on other words.

# Given a password and a word returns a regional expressional that will match the decoded word
# Can be used to exclude decoded word candidates

def make_lookup_table():
    lookup = dict()
    inputfile = open('dictionary.lst', 'r')

    for word in inputfile.readlines():
        word = word.replace('\n', '').lower()
        freq = []
        for letter in word:
            freq.append(round(float(word.count(letter)) / len(word), 4))
        
        lookup[word] = freq

    inputfile.close()
    return lookup

def get_regexp(pwd, encoded_word):  
    regex = ""

    for letter in encoded_word:
        regex += pwd[ord(letter) - ord('a')]

    return regex + '$'


def try_to_updatepwd(pwd, encoded_word, candidates):
    regex = get_regexp(pwd, encoded_word)
    match = re.compile(regex)
    decoded_word = None
    correct_candidates = []

    for candidate in candidates:
        if match.match(candidate) != None:
            correct_candidates.append(candidate)
            
    if len(correct_candidates) == 1:
        # print "found:\t", encoded_word, "-->", correct_candidates[0]
        pwd = updatepwd(pwd, encoded_word, correct_candidates[0])
        decoded_word = correct_candidates[0]
    # else:
        # print "Too many candidates:\t", encoded_word, "-->", correct_candidates

    return (pwd, decoded_word)

def updatepwd(pwd, encoded_word, decoded_word):

    for i in range(len(encoded_word)):
        index = ord(encoded_word[i]) - ord('a')
        pwd[index] = decoded_word[i].encode("utf8")

    return pwd


def decode_text(pwd, original_text):
    new_text = ""

    for letter in original_text:
        if letter == ' ':
            new_letter = ' '
        else:
            new_letter = pwd[ord(letter) - ord('a')]
        new_text += new_letter

    return new_text

t1 = time.clock()


lookup = make_lookup_table()

sample = open('newtestcase-encoded.txt', 'r')
original_text = sample.readline()




pwd_list = [chr(i + ord('a')) for i in range(26)]
pwd = ['.'] * 26

decode = dict()
done = False

for runs in xrange(2):
    if done:
        break
    words = original_text.split(' ')
    for word in words:
        distr = []
        for letter in word:
            cnt = word.count(letter)
            distr.append(round(float(cnt) / len(word), 4))

        candidates = []
        for key, distribution in lookup.iteritems():
            if distribution == distr:
                candidates.append(key)
        
        if len(candidates) == 1:
            decoded_word = candidates[0]
            pwd = updatepwd(pwd, word, decoded_word)
            # print "found:\t", word, "-->", decoded_word
            decode[word] = decoded_word
        elif len(candidates) > 1:
            (pwd, decoded_word) = try_to_updatepwd(pwd, word, candidates)
            if decoded_word != None:
                decode[word] = decoded_word

        done = not '.' in pwd



# print "ref: ", pwd_list
# print "pwd: ", pwd
outputfile = open('test.txt', 'w')
outputfile.write(decode_text(pwd, original_text))

t2 = time.clock()
# print "delta:", t2 - t1

outputfile.close()
sample.close()



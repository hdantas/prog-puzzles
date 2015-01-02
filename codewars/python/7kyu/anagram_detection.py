# http://www.codewars.com/kata/529eef7a9194e0cbc1000255

def is_anagram(test, original):
    if(len(test) != len(original)):
        return False
    tokens = list(test.lower())
    for t in tokens:
        count_test = test.lower().count(t)
        count_original = original.lower().count(t)

        if (count_test != count_original):
            return False

    return True
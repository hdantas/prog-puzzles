# http://www.codewars.com/kata/545cdb4f61778e52810003a2

def levenshtein(a,b):
    indexb = 0
    result = 0

    for c_a in a:
        if indexb >= len(b):
            result -= 1
            break
        elif c_a != b[indexb]:
            result += 1

        indexb += 1

    return result + abs(len(a) - len(b))
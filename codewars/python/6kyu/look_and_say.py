# http://www.codewars.com/kata/53ea07c9247bc3fcaa00084d

def look_and_say(data='1', maxlen=5):
    toprint = data
    result = []
    for i in xrange(maxlen):
        counter = 1
        new_str = ""
        for index in xrange(len(toprint) - 1):
            if toprint[index] != toprint[index + 1]:
                new_str += str(counter) + toprint[index]
                counter = 1
            else:
                counter += 1

        toprint = new_str + str(counter) + toprint[-1]
        result += [toprint]

    return result
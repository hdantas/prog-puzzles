# http://www.codewars.com/kata/5417423f9e2e6c2f040002ae

def digitize(n):
    tmp_n = n
    result = []

    if (tmp_n == 0):
        return [0]
    while(tmp_n > 0):
        if(tmp_n % 10 >= 0):
            result = [tmp_n % 10] + result
        tmp_n /= 10
    return result
import sys
import operator
import logging

limit = 1000000009

def do_work(length_H, length_X, array_H, array_X):
    logging.debug("H: %s", array_H)
    logging.debug("X: %s", array_X)
    result = 0

    for i in xrange(length_H):
        hterm_1 = array_H[i] % limit
        for j in xrange(i + 1, length_H):
            hterm_2 = array_H[j] % limit
            tmp = 0
            # for k in xrange(length_X):
                # xterm_1 = array_X[i][k]
                # xterm_2 = array_X[j][k]
                # tmp += (abs(xterm_1 - xterm_2)) % limit
                
                # if tmp_abs < 0: tmp += -tmp_abs
                # else: tmp += tmp_abs
            tmp = (
                abs(array_X[i][0] - array_X[j][0])  % limit +
                abs(array_X[i][1] - array_X[j][1])  % limit +
                abs(array_X[i][2] - array_X[j][2])  % limit +
                abs(array_X[i][3] - array_X[j][3])  % limit
                ) % limit
            result += (hterm_1 * hterm_2 * tmp) % limit

        logging.debug("result += %d * %d * dist\tresult = %s", H[i], H[j], result)
    print result % limit


if sys.platform == 'darwin':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    n = 6
    d = 4
    H = [539608, 386259, 292996, 449841, 23204, 804119]
    X = [
            [-165717, 805898,  -996738, 671609],
            [285915,  -791994, -425124, 93519],
            [-332687, -520472, 666331,  662144],
            [-187201, 675577,  -936931, -91675],
            [955059,  -285301, -646370, -585216],
            [-26775,  918480,  595955,  657667]
        ]

    do_work(n, d, H, X)
    exit()

    logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
    myfile = open("input04.txt")
    [n, d] = map(int, myfile.readline().split())
    H = [0] * n
    X = [[0] * d] * n

    for i in xrange(n):
        tmp = map(int, myfile.readline().split())

        H[i] = tmp[0]
        X[i] = tmp[1: d + 1]
    do_work(n, d, H, X)

else:
    [n, d] = map(int, raw_input().split())
    H = [0] * n
    X = [[0] * d] * n

    for i in xrange(n):
        tmp = map(int, raw_input().split())

        H[i] = tmp[0]
        X[i] = tmp[1: d + 1]
    do_work(n, d, H, X)

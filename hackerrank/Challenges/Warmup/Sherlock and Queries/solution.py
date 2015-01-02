import cProfile
import time

f2 = open('output0.txt')
answer = f2.readline()

f = open('input0.txt')
s = f.readline()
n,m = [int(i) for i in s.split(' ')]
n /= 1
m /= 1
a = [0] + [int(i) for i in f.readline().split(' ')]
b = [0] + [int(i) for i in f.readline().split(' ')]
c = [0] + [int(i) for i in f.readline().split(' ')]
MOD = 1000000007

counti = [-1] * 100006

def hack():
    for i in xrange(1, m + 1):
        if counti[b[i]] == -1:
            counti[b[i]] = c[i]
        else:
            counti[b[i]] = (counti[b[i]] * c[i]) % MOD

    for i in xrange(1, n + 1):
        j = 1
        while (j * i) <= n:
            if counti[i] != -1:
                a[j * i] = (a[j * i] * counti[i]) % MOD;
                print "a[%d] = (a[%d] * counti[%d]) %% MOD" % (j*i, j*i, i);
            j += 1






t1 = time.clock()
hack()
t2 = time.clock()
print "run time: ", round(t2 - t1, 3)

result =  ' '.join([str(a[j]) for j in xrange(1, n + 1)])
# print result
print answer == result
f.close()
f2.close()
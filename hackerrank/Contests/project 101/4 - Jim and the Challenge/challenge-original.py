### author: jim
### problem: the challenge
### status: TLE

mod = 1000000009
def m(i, j):
    dist = 0
    
    for k in range(d):
        dist += abs(X[i][k] - X[j][k])
    return dist


myfile = open("input03.txt")
[n, d] = map(int, myfile.readline().split())
H = [0] * n
X = [[0] * d] * n

for i in xrange(n):
    tmp = map(int, myfile.readline().split())

    H[i] = tmp[0]
    X[i] = tmp[1:]


# tmp = raw_input().split(' ')
# n = int(tmp[0])
# d = int(tmp[1])

# H = [0] * (n + 1)
# X = [0] * (n + 1)

# for i in range(1, n + 1):
#     tmp = raw_input().split(' ')
#     H[i] = int(tmp[0])
#     X[i] = map(int, tmp[1:])


sum = 0

for i in range(n):
    for j in range(i + 1, n):
        sum += (H[i] * H[j] * m(i, j)) % mod

print sum % mod
from datetime import datetime

limit = 10000000000

def do_work(n):
	x = 0
	for i in range(1, n+1):
		x += pow(i, i, limit)
		# x = pow(i, i, limit)
	return x % limit

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())

startTime = datetime.now()
print do_work(n)
print(datetime.now()-startTime)
    
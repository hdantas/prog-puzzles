

def do_work(n):
    response = []
    for i in range(len(n)):
        t = int(n[i][0])
        d = int(n[i][1])
        response += [i + 1, d + t], 
    
    sorted_x = sorted(response, key=lambda student: student[1])
    
    for i in range(len(n)):
        print sorted_x[i][0],



inp = []
n = int(raw_input())

for i in range(n):
    string = raw_input()
    val = string.split();
    inp.append(val)

do_work(inp)
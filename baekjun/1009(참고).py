import sys

T = int(input())
ans = []
for _ in range(T):
    a, b= map(int, sys.stdin.readline().split())

    ret = []

    tmp = 1
    for _ in range(b):
        tmp *= a
        tmp %= 10

        if tmp in ret:
            break
        ret.append(tmp)

    cycle = len(ret)      
    idx = (b % cycle) - 1
    
    if ret[idx] == 0:
        ans.append(10)
    else:
        ans.append(ret[idx])

for i in ans:
    print(i)
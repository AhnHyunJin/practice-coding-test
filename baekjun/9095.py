T = int(input())

ans= []

for _ in range(T):
    n = int(input())
    d = [0,1,2,4]
    for i in range(4,n+1):
        d.append(d[i-3] + d[i-2] + d[i-1])
    ans.append(d[n])

for n in ans:
    print(n)
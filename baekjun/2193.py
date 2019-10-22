N = int(input())

d = [0,1,1]

if N == 1 or N == 2:
    print(d[N])
else:
    for i in range(3,N+1):
        d.append(d[i-2] + d[i-1])
    print(d[N])
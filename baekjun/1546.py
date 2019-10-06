import sys
N = int(input())
a = list(map(int, sys.stdin.readline().split(' ') ))
a.sort()
sum = 0
for i in a:
    sum += i

M = a[N-1]
print(M)
print(sum)
avg = ((100/M) * sum ) / N

print(avg)
import sys
ans = 0
for i in range(11):
    d,v = map(int, sys.stdin.readline().split(' '))
    ans += d* (v+1) + 20 * v 
print(ans)
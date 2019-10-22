#다시 풀어볼 것

n = int(input())

_memo = [0] * (n+1)

_memo[1] = 1
_memo[2] = 3

ans = 0

def memoization(n):
    ans = 0
    tmp = 0
    for i in range(1,n):
        #for j in range(n-i, 0,-1):             
        tmp = _memo[i] + _memo[n-i]
    ans += tmp 
    return ans

#make _memo
for i in range(3,n+1):
    _memo[i] = memoization(i)

print(_memo[n])
import sys

N = int(input())
s = list(map(int, sys.stdin.readline().split(' ')))

dp = [0] * N


for i in range(0, N):
    for j in range(i):
        if s[i] > s[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1
print(max(dp))

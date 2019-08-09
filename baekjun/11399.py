N = int(input())
M = [int(x) for x in input().split()]

M.sort()

subsum = []

subsum.append(M[0])

for x in range(1,N):
    subsum.append(subsum[x-1] + M[x])

ret = sum(subsum)
print(ret)
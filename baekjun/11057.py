N = int(input())

arr = [[0] * 10  for _ in range(N+1)]

for i in range(10):
    arr[1][i] = 1


for i in range(2, N+1):
    for j in range(10):
        tmp = 0        
        for k in range(0,j+1):
            tmp += arr[i-1][k]
        arr[i][j] = tmp


ans = 0
for i in range(10):
    ans += arr[N][i]
print(ans % 10007)
import sys
from collections import deque
sys.setrecursionlimit(10000)

T = int(input())
cnt = 0
max_size = 1004

def dfs(start,N):
    global cnt
    if c[start]:
        return

    c[start] = True
    for adj in range(N + 1):
        if (a[start][adj] or a[adj][start]) and (not c[adj]):
            cnt +=1
            dfs(adj,N)
    


for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    c = [False] * max_size
    a = [[False for _ in range(max_size)] for _ in range(max_size)]

    for _ in range(M):
        x,y = map(int, sys.stdin.readline().split())
        a[x][y] = True
        a[y][x] = True

    dfs(1,N)
    
    print(cnt)
    cnt =0



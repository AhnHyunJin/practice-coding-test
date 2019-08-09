from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
a = [list(input().strip())for _ in range(n)]
check = [[False]*n for _ in range(n)]
dx = (-1,0,1,0)
dy = (0,1,0,-1)

def bfs(i,j,c,w):
    q = deque()
    q.append((i,j))
    check[i][j] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x+ dx[k], y+ dy[k]
            if n <0 or nx >=n or ny<0 or ny>=n or check[nx][ny]:
                continue
            if w is True and c == 'B' and (a[nx][ny] == 'R' or a[nx][ny]=='G'):
                continue
            if w is True and c!='B'and a[nx][ny] == 'B':
                continue
            if w is False and a[nx][ny] != c:
                continue
            q.append((nx,ny))
            check[nx][ny] = True

cnt = 0
for i in range(n):
    for j in range(n):
        if check[i][j] is False:
            bfs(i,j,a[i][j], False)
            cnt +=1
print(cnt, end=' ')

cnt = 0
check = [[False]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if check[i][j] is False:
            bfs(i,j,a[i][j],True)
            cnt +=1

print(cnt)
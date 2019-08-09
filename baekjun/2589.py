from collections import deque
import sys

h, w = map(int, sys.stdin.readline().split())

map_arr= [[x for x in input()] for _ in range(h) ]
visited = [[False for _ in range(w)] for _ in range(h)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    q = deque()
    dist= 0
    q.append([x,y,dist])
    visited[x][y] = True    
    
    while q:              
        x,y,d = q.popleft()
        for n in range(4):                                       
            nx = x + dx[n]
            ny = y + dy[n]

            if nx < 0 or nx >= h or ny <0 or ny >= w:
                continue
            if visited[nx][ny] == False and map_arr[nx][ny] == "L":
                visited[nx][ny] = True                            
                tmp=[nx,ny,d+1]
                q.append(tmp)
                dist = max(d+1,dist)
        
    return dist

res = 0
for i in range(h):
    for j in range(w):
        if map_arr[i][j] == 'L':
            tmp = bfs(i,j)
            visited = [[False for _ in range(w)] for _ in range(h)]
            res = max(res, tmp)

print(res)
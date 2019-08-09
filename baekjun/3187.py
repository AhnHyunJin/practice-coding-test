import sys
from collections import deque

R,C = map(int, sys.stdin.readline().split())

area = []

for _ in range(R):
    area.append(input())


visited = [[False for _ in range(C)] for _ in range(R)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

total_k = 0
total_v = 0

def bfs(i,j):
    q = deque()
    if area[i][j] == '#':
        return
    q.append([i,j])
    num_k = 0
    num_v =0
    global total_k, total_v    
    visited[i][j] = True

    while(q):
        x,y = q.popleft()
        
        
        if area[x][y] == "v":
            num_v += 1

        elif area[x][y] == "k":    
            num_k += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0 or area[nx][ny] == "#":
                continue
            else:
                if not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                
    if num_k > num_v:
        total_k += num_k
    else:
        total_v += num_v

for i in range(R):
    for j in range(C):
        if visited[i][j] == False:
            bfs(i,j)

print(total_k, total_v)
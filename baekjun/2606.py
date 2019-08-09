from collections import deque

num_of_com = int(input()) + 1
num_of_edge = int(input())

edge_arr = [[False for _ in range(num_of_com)] for _ in range(num_of_com)]
visited = [False for _ in range(num_of_com)]

#edge array 생성 bfs 에서 연결 여부 확인 시 사용할 것
for _ in range(num_of_edge):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    edge_arr[x][y] = True
    edge_arr[y][x] = True

def bfs(s):
    cnt = 0
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        pos = q.popleft()
        cnt += 1
        tmp = []
        for i in range(num_of_com):        
            if edge_arr[pos][i] and (not visited[i]):
                tmp.append(i)
                visited[i] = True
                
            else:
                continue

        for x in tmp:
            q.append(x)
        tmp.clear()
    print(cnt-1)

bfs(1)
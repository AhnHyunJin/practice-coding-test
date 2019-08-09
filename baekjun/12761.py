import sys
from collections import deque

A,B,N,M = map(int, sys.stdin.readline().split())

max_num = 100002


c = [False] * max_num

nx = N



def bfs(start,dist):
    q = deque()
    q.append([start,dist])
    c[start] = True
    while(q):        
        x,d = q.popleft()
        
        nx = [x+1, x-1, x+A, x-A, x+B, x-B, A*x, B*x]
    
        if x == M:                
            return d

        for x in nx: 
            if x >100000 or x <0 or c[x]:
                continue

            else:                
                q.append([x,d+1])
                c[x] = True
                
    

print(bfs(N,0))
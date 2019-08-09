import sys

N,M,start = map(int, sys.stdin.readline().split())

map_array = [ [0]*N for i in range(N) ]

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    map_array[i-1][j-1] = 1


def dfs():
    

def bfs():

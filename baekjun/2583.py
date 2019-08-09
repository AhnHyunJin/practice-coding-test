from collections import deque
import sys

M,N,K = map(int, sys.stdin.readline().split())

#M - 세로, N - 가로
area = [[False in range(N)] in range(M)]


for _ in range(K):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())


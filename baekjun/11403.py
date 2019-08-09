import sys
sys.setrecursionlimit(10000)
N = int(input())

tmp = []
a = []
c = [False] * N
ret = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)


def dfs(start):
    global c
    for adj in range(N):        
        if a[start][adj] == 1 and (adj != start) and not c[adj]:
            c[adj] = True
            dfs(adj)
    

def dfs_all():
    global c
    for s in range(N):        
        dfs(s)
        for i in range(N):
            if c[i]:
                ret[s][i] = 1
        c = [False] * N        
    return ret

ans = dfs_all()

for i in range(N):
    _str = ""
    for j in range(0,N):
        _str += str(ans[i][j]) + " "
    print(_str)
    
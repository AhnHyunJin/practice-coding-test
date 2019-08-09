import sys

N = sys.stdin.readline()
N = int(N)
map_arr = [[x for x in input()] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


nx = [0,1,0,-1]
ny = [1,0,-1,0]

cnt_area = 0
num_of_house = []
cnt_houses=0


def dfs(x,y):    
    if visited[x][y]:              
        return
    else:
        visited[x][y] = True
        global cnt_houses        
        cnt_houses += 1
        
        for i in range(4):
            if x + nx[i] >= N or x + nx[i] <0 or y + ny[i] >=N or y + ny[i] <0 or visited[x+nx[i]][y+ny[i]]:                    
                continue
            else:
                if map_arr[x+nx[i]][y+ny[i]] =='1':
                    
                    dfs(x+nx[i], y+ny[i])



for i in range(N):
    for j in range(N):
        if map_arr[i][j] == '1' and not visited[i][j]:
            
            dfs(i,j)
            cnt_area += 1
            
            num_of_house.append(cnt_houses)
            cnt_houses = 0


print(cnt_area)
num_of_house.sort()
for i in num_of_house:
    print(i)


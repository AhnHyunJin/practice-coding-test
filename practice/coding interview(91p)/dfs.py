
def dfs(start):
    
    s = []
    s.append(start)
    ret = []   
    
    if visited[start]:
        return
    visited[start] = True
    print(start)
    
    tmp = graph[start]
    for adj in tmp:
        dfs(adj)

if __name__ == "__main__":
    
    graph = {
        1:[2,3],
        2:[3,4,5],
        3:[2,6,7],
        4:[2,5],
        5:[2,4],
        6:[3,7],
        7:[3,6]
    }
    visited = [False for _ in range(8)]
    print(dfs(1))

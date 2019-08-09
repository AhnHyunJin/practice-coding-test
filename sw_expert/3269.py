graph = {
    1: [4,6],
    2: [7],
    3: [7],
    4: [5],
    5: [1],
    6: [7],
    7: [2,3,9]
}

def dfs(graph, s):
    visited = []
    tovisit = [s]

    u = graph[tovisit[0]]

    for i in u:
        visited.append[i]    
        while i not in visited + tovisit:
            
            dfs(graph, i)
    
    return visited

print(dfs(graph, 1))
def BFS(adj, s):
    discovered = [s]
    processed = []
    layer = {s:0}
    while discovered:
        u = discovered.pop(0)
        processed.append(u)
        for i in adj[u]:
            if i not in discovered + processed:
                discovered.append(i)
                layer[i] = layer[u] + 1
    return processed, layer
G1 = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6], 6:[], 7:[8], 8:[]}
print BFS(G1, 1)
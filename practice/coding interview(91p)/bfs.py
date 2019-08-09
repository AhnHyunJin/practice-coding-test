from collections import deque

def bfs(start):
    q = deque()
    visited = [False for _ in range(8)]
    
    q.append(start)
    while(q):
        pos = q.popleft()
        print(pos)
        try:
            for i in graph[pos]:            
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        except KeyError:
            continue

if __name__ == "__main__":
    graph = {
        1:[2,3],
        2:[4,5],
        3:[6,7]
    }
    bfs(1)

    


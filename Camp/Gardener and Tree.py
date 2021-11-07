from collections import deque
def removeLeaves():
    testCases = int(input())
    for i in range(testCases):
        input()
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        graph = [[] for _ in range(n)]
        edges = [0] * n
        for _ in range(n - 1):
            uv = input().split()
            u = int(uv[0])
            v = int(uv[1])
            graph[u - 1].append(v)
            graph[v - 1].append(u)
            edges[u - 1] += 1
            edges[v - 1] += 1
            
        queue = deque([i + 1 for i in range(len(edges)) if edges[i] <= 1])
        
        while k and queue:
            size = len(queue)
            n -= size
            for _ in range(size):
                curr = queue.popleft()
                for node in graph[curr - 1]:
                    edges[node - 1] -= 1
                    if edges[node - 1] == 1:
                        queue.append(node)
            k -= 1
        print(n)

removeLeaves()
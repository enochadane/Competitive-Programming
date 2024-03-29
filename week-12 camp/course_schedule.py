class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for i in range(n)]
        degree = [0]*n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(len(degree)) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        
        return len(bfs) == n

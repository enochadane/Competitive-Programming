class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        adj_list = {}
        visited = set()
        for y in range(len(isConnected)):
            connections = []
            for x in range(len(isConnected[y])):
                if isConnected[y][x] == 1:
                    connections.append(x)
            adj_list[y] = connections
        print(adj_list)
        for k, v in adj_list.items():
            count += self.dfs(adj_list, k, visited)
        
        return count
    
    def dfs(self, adj_list: dict, k: int, visited) -> int:
        if k not in visited:
            visited.add(k)
            for v in adj_list[k]:
                self.dfs(adj_list, v, visited)
            return 1
        return 0
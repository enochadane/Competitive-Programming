from collections import defaultdict
input()
def repostChain():
    reposts = int(input())
    graph = defaultdict(list)
    for _ in range(reposts):
        chain = input().split()
        graph[chain[2].lower()].append(chain[0].lower())
    print(graph)

    def dfs(person):
        depth = 0
        if not graph[person]:
            return 1
        for poster in graph[person]:
            depth = max(depth, 1 + dfs(graph[poster]))
        return depth
    return dfs('polycarp')

repostChain()

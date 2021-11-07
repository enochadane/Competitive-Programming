from collections import deque
def transportation():
    nd = list(map(int, input().split()))
    ports = list(map(int, input().split()))
    n = nd[0]
    dest = nd[1]
    q = deque([1])
    canReach = False
    while q:
        index = q.popleft()
        if index == dest:
            canReach = True
            break
        if index >= n:
            break
        nxt = index + ports[index - 1]
        q.append(nxt)
    if canReach:
        print("YES")
    else:
        print("NO")

transportation()
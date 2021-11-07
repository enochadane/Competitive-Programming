from collections import deque
from collections import deque
def chess():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    if (c[0] > a[0] and b[0] < a[0]) or (c[1] > a[1] and b[1] < a[1]):
        print("NO")
    elif (c[0] < a[0] and b[0] > a[0]) or (c[1] < a[1] and b[1] > a[1]):
        print("NO")
    else:
        print("YES")

chess()


# def chess():
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     c = list(map(int, input().split()))
#     q = deque([(b[0], b[1])])
#     visited = {(b[0], b[1])}
#     canReach = False
#     while q:
#         bx, by = q.popleft()
#         if bx == c[0] and by == c[1]:
#             canReach = True
#             break
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
#         for dr in directions:
#             new_bx = bx + dr[0]
#             new_by = by + dr[1]
#             if isValid(n, new_bx, new_by, a[0], a[1]) and (new_bx, new_by) not in visited:
#                 visited.add((new_bx, new_by))
#                 q.append((new_bx, new_by))
#     if canReach:
#         print("YES")
#     else:
#         print("NO")
# def isValid(n, x, y, ax, ay):
#     if (0 <= x < n) and (0 <= y < n) and (x != ax) and (y != ay) and (abs(ax - x) != abs(ay - y)):
#         return True
#     return False

# chess()
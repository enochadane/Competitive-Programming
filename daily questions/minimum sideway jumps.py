from collections import deque
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        seen = [[False for _ in range(len(obstacles))] for _ in range(3)]
        q = deque([(2, 0, 0)])
        seen[1][0] = True
        while q:
            lane, point, jumps = q.popleft()
            nextLane = 0
            if point == len(obstacles) - 1:
                return jumps
            elif obstacles[point + 1] != lane and not seen[lane - 1][point + 1]:
                q.append((lane, point + 1, jumps))
                seen[lane - 1][point + 1] = True
            else:
                for newLane in range(1, 4):
                    if newLane != obstacles[point] and newLane != obstacles[point + 1] and not seen[newLane - 1][point]:
                        q.append((newLane, point, jumps + 1))
                        seen[newLane - 1][point] = True
        
        return jumps
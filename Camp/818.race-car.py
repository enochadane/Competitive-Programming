#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#

# @lc code=start
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            if 0 < pos + speed <= 10000:
                queue.append((pos + speed, speed * 2, steps + 1))
            if speed > 0 and pos + speed > target:
                queue.append((pos, -1, steps + 1))
            elif speed < 0 and pos + speed < target:
                queue.append((pos, 1, steps + 1))
# @lc code=end


import collections
class Solution:
    def racecar(self, target: int) -> int:
        count = 0
        start = (0, 1)
        queue = collections.deque()
        queue.append(start)
        while queue:
            race = queue.popleft()
            position = race[0]
            speed = race[1]
            if position == target:
                return count
            elif position < target or speed < 0:
                queue.append((position + speed, speed *2))
                count +=1
            else:
                if speed > 0:
                    speed = -1
                else:
                    speed = 1
                queue.append((position, speed))
                count +=1
        return count
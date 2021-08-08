class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=y=0
        res = 0
        d = 0
        obs = {(a, b): True for a, b in obstacles}
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            elif 1 <= c <= 9:
                if d == 0:
                    while c > 0 and obs.get((x, y + 1), False) == False:
                        y += 1
                        c -= 1
                elif d == 1:
                    while c > 0 and obs.get((x + 1, y), False) == False:
                        x += 1
                        c -= 1
                elif d == 2:
                    while c > 0 and obs.get((x, y - 1), False) == False:
                        y -= 1
                        c -= 1
                else:
                    while c > 0 and obs.get((x - 1, y), False) == False:
                        x -= 1
                        c -= 1
            res = max(res, x**2 + y**2)
            
        return res
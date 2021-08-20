class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s = "ADOBECODEBANC", t = "ABC"
        cnt = defaultdict(int)
        nUnique = 0
        for c in t:
            if cnt[c] == 0: nUnique += 1
            cnt[c] += 1

        l = 0
        while l < len(s) and cnt[s[l]] == 0: l += 1  # Firstly, let `l` point to a char in `t` string
        ans, ansStart = len(s) + 1, -1
        for r, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                nUnique -= 1
                if nUnique == 0:  # Already removed all characters in `t` -> Update answer
                    if ans > r - l + 1:
                        ans = r - l + 1
                        ansStart = l
                    cnt[s[l]] += 1  # Jump a letter
                    l += 1
                    nUnique += 1

            while l <= r and cnt[s[l]] < 0:  # Move left util cnt[s[l]] == 0
                cnt[s[l]] += 1
                l += 1

        if ansStart == -1: return ""
        return s[ansStart: ansStart + ans]
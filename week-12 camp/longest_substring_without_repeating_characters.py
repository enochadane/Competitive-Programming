class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_ = 0
        left = 0
        right = 0
        while left < len(s) and right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
                max_ = max(max_, right - left)
            else:
                visited.remove(s[left])
                left += 1
            
        return max_
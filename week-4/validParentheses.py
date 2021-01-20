class Solution:
    def isValid(self, s: str) -> bool:
        openings = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c is not openings[stack.pop()]:
                    return False
        return len(stack) == 0
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s= [char for char in s]
        letters = []
        output = [None]*len(s)
        for i in range(len(s)):
            if (65 <= ord(s[i]) <= 90) or  (97 <= ord(s[i]) <= 122):
                letters.append(s[i])
            else:
                output[i] = s[i]
        for i in range(len(output)):
            if output[i] is None:
                c = letters.pop()
                output[i] = c
            else:
                continue
        return ''.join(output)
            
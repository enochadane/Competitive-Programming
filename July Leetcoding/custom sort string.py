class Solution:
    def customSortString(self, order: str, str: str) -> str:
        order = [c for c in order]
        str = [c for c in str]
        output = []
        for char in order:
            for i in range(len(str)):
                if str[i] == char:
                    output.append(char)
        for char in str:
            if not char in order:
                output.append(char)
                
        return ''.join(output)
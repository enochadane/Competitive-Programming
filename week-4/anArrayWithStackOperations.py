class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        for i in range(1, target[-1] + 1, 1):
            output.append("Push")
            if i not in target:
                output.append("Pop")
        return output
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        checked = set()
        for i in range(len(strs) - 1):
            str_ = strs[i]
            for j in range(len(str_)):
                if str_[j] > strs[i + 1][j] and j not in checked:
                    checked.add(j)
        return len(checked)
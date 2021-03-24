class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = []
        sum_ = [(sum(mat[i]), i) for i in range(len(mat))]
        sum_ = sorted(sum_, key = lambda row: row[0])
        for i in range(k):
            output.append(sum_[i][1])
        return output
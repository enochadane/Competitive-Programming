class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while K > 0 and i < len(A):
            if A[i] < 0:
                A[i] *= -1
                K -= 1
            else:
                min_ = min(A)
                if K % 2 == 0:
                    break
                else:
                    sum_ = sum(A)
                    return sum_ - (min_ * 2)
            i += 1
        return sum(A)
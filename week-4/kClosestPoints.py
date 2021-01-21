class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        output = []
        sortedPoints = sorted(points, key = lambda point: (point[0]) ** 2 + (point[1]) ** 2)
        for i in range(K):
            output.append(sortedPoints[i])
        return output

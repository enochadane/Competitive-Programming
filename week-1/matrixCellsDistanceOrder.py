class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        outputMatrix = []
        order = []
        for r in range(R):
            for c in range(C):
                outputMatrix.append([r, c])
                dist_r = r0 - r
                dist_c = c0 - c
                if dist_r < 0:
                    dist_r = -1 * dist_r
                if dist_c < 0:
                    dist_c = -1 * dist_c
                order.append(dist_r + dist_c)
        for i in range(len(order)):
            min = i
            for j in range(i + 1, len(order), 1):
                if order[j] < order[min]:
                    min = j
            if min != i:
                order[i], order[min] = order[min], order[i]
                outputMatrix[i], outputMatrix[min] = outputMatrix[min], outputMatrix[i]
        
        return outputMatrix

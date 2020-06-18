import math

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for row in matrix:
            res.extend(row)
        
        res = sorted(res)
        return res[k-1]
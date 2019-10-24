class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ln = len(cost)
        if ln <= 1 or ln > 1000:
            return -1
        tc = [''] * ln
        tc[0], tc[1] = cost[0], cost[1]
        for i in range(2,ln):
            tc[i] = min(tc[i-2],tc[i-1]) +cost[i]
        
        return min(tc[-1],tc[-2])
        
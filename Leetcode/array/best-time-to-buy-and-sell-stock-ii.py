class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr, prev, profit, max_pr = 0, 0, 0, 0
        for index, n in enumerate(prices):
            if index == 0:
                min_pr = n
                prev = n
            elif prev > n:
                min_pr = n
                max_pr += profit
                profit, prev = 0, n
            elif profit <= (n-min_pr):
                profit = n-min_pr
                # print(profit)
                prev = n
                if index == len(prices)-1:
                    max_pr += profit
        
        return max_pr
        
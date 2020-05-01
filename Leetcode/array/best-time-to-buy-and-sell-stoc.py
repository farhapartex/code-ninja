class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr, max_pr, profit = 0, 0, 0
        for index, n in enumerate(prices):
            if n <= min_pr:
                min_pr = n
            elif n > min_pr:
                if index == 0:
                    min_pr = n
                if profit < (n-min_pr):
                    profit = n-min_pr
        
        return profit
        
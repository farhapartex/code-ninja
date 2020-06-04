class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        ph = len(candies)//2
        kind = len(set(candies))
        
        return ph if kind>=ph else kind
            
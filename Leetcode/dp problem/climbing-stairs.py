class Solution:
    def __init__(self):
        self.dict = {1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        val = self.climbStairs(n-1)
        self.dict[n-1] = val
        
        return self.dict[n-2] + val
        
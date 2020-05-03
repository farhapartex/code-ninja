import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ran = int(math.sqrt(c))
        for n in range(0,ran+1):
            n = n**2
            m = c- n
            if int(math.sqrt(m))**2 == m:
                return True
        
        return False
        
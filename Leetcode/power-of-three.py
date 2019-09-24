from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        r = log(n)/log(3)
        return (abs(round(r) - r) < 10**-10)
        
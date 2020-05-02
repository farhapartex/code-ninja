import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 0:
            return False
        elif num == 0:
            return False
        
        p , r = 0, int(math.sqrt(num))
        for i in range(1, r+1):
            if num%i==0:
                if num//i == i:
                    p += i
                else:
                    p += (i + (num//i))
        p -= num
        
        return True if p == num else False
        
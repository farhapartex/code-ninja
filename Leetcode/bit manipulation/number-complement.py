import math

class Solution:
    def complement_number(self, n):
        number_of_bits = (int)(math.floor(math.log(n) / math.log(2))) + 1        
        return ((1 << number_of_bits) - 1) ^ n
    
    def findComplement(self, num: int) -> int:
        return self.complement_number(num)
        
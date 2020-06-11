class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num = bin(n)[2:]
        prev = "0"
        for n in bin_num:
            #print(n)
            if n == prev:
                return False
            prev = n
        
        return True
        
class Solution:
    def subtractProductAndSum(self, num: int) -> int:
        prod, add = 1, 0
        
        for n in str(num):
            prod *= int(n)
            add += int(n)
            
        return prod-add
        
class Solution(object):
    
    def get_summation(self,nums):
        res=0
        for n in nums:
            res = (res*10) + n 
        return res +1
    
    def plusOne(self, digits):
        data=[]
        res = self.get_summation(digits)
        while res != 0:
            d = res%10
            data.append(d)
            res = res/10
        data = data[::-1]
        return data
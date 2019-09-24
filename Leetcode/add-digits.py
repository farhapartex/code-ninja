class Solution:
    def get_sum(self,num):
        res=0
        for s in num:
            res += int(s)
        return res
    
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
                return num
        while True:
            num = self.get_sum(str(num))
            if len(str(num))==1:
                return num
            
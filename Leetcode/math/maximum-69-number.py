class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = str(num)
        for index in range(0,len(temp)):
            if temp[index] == '6':
                return num + int('3'+'0'*(len(temp)-index-1))
        
        return num
        
        
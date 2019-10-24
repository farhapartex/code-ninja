class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        carry = 0
        if len(num1) > len(num2):
            mx_num = num1
            mn_num = num2
        else:
            mx_num = num2
            mn_num = num1
        
        i,j = 0, 0
        single_num = False
        data = []
        
        while True:
            if i == len(mx_num):
                if carry > 0:
                    data.append(carry)
                break
            if j >= len(mn_num):
                single_num = True
            
            if single_num:
                val = int(mx_num[i]) + carry
            else:
                val = int(mx_num[i]) + int(mn_num[j]) + carry
                
            if val > 9:
                data.append(val %10)
                carry = int(val/10)
            else:
                carry = 0
                data.append(val)
            i+=1
            j+=1
        
        num=''
        for n in data:
            num += str(n)
        return num[::-1]
        
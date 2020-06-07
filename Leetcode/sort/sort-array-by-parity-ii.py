class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        data = [0]*len(A)
        
        for n in A:
            if n&1==0:
                data[even] = n
                even += 2
            else:
                data[odd] = n
                odd += 2
        
        return data
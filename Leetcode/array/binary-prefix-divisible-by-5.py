class Solution:
        
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        pre = 0
        for i in range(len(A)):
            pre = pre << 1
            curr = pre + A[i]
            if curr%5 == 0:
                A[i] = True
            else:
                A[i] = False
            pre = curr
        
        return 
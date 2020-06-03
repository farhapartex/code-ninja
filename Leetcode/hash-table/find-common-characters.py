class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if len(A)==1:
            return list(A[0])
        
        for ch in A[0]:
            flag=False
            for index in range(1,len(A)):
                if ch in A[index]:
                    A[index] = A[index].replace(ch,"",1)
                else:
                    flag=True
                
            if not flag:
                res.append(ch)
        return res
        
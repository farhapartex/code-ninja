class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A[:], per = sorted(A), -1
        
        for index in range(len(A)-1,1,-1):
            a,b,c = A[index-2:index+1]
            if c < b+a:
                return sum(A[index-2:index+1])
        
        return 0
        
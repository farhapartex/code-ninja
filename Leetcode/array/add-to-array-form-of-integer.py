class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return map(int, str(int("".join(map(str,A))) + K))
#         num = 0
#         for i in range(len(A)):
#             num += (A[i] * 10**(len(A[i+1:])))
        
#         num += K
#         return [int(ch) for ch in str(num)]
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        temp = ""
        for ch in S:
            n = T.count(ch)
            T = T.replace(ch, "")
            temp = temp +(ch*n)
        
        return temp+T
        
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        
        for i, st in enumerate(s):
            if st != t[i]:
                return t[i]
        
        return t[-1]
        
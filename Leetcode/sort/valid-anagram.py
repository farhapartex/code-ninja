class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        data = {chr(n):0 for n in range(ord('a'), ord('z')+1, 1)}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            data[s[i]] += 1
            data[t[i]] -= 1
        
        
        for k in data.keys():
            if data[k]>0:
                return False
        
        return True
        
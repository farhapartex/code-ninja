class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = 0, 0
        if s == "" and (t== "" or len(t)>0):
            return True
        
        
        while m<len(s) and n<len(t):
            if s[m] == t[n]:
                #print(m)
                m, n = m+1, n+1
            else:
                n+=1
        #print(m)
        return True if m >= len(s) else False
        
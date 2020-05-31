class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        if len(s)==0: return True
        s = s.lower()
        i, ln = 0, len(s)-1
        
        while i <= ln:
            if s[i].isalnum() and s[ln].isalnum():
                if s[i] == s[ln]:
                    i+=1
                    ln -= 1
                else:
                    return False
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[ln].isalnum():
                    ln -= 1
        
        return True

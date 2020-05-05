class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        d1 = []
        for ch in list(S):
            if ch == "#" and len(d1) == 0:
                continue
            d1.pop() if ch == "#" else d1.append(ch)
        s1 = "".join(d1)
        d1 = []  
        
        for ch in list(T):
            if ch == "#" and len(d1) == 0:
                continue
            d1.pop() if ch == "#" else d1.append(ch)
        
        t1 = "".join(d1)
        
        return True if s1 == t1 else False
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        data = {}
        for index, ch in enumerate(s):
            if ch not in data:
                if t[index] in data.values():
                    return False
                else:
                    data[ch] = t[index]
            elif data[ch] != t[index]:
                return False
        
        return True
        
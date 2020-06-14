class Solution:
    def check_pattern(self, s, t):
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
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.check_pattern(word, pattern):
                res.append(word)
        
        return res
        
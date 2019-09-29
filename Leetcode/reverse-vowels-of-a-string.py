class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        
        data = []
        for ch in s:
            if ch in vowel:
                data.append(ch)
        data = data[::-1]
        res=""
        
        for i in range(len(s)):
            if s[i] in vowel:
                res += data.pop(0)
            else:
                res += s[i]
        return res
                
        
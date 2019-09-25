class Solution:
    def titleToNumber(self, s: str) -> int:
        num=0
        for ch in s:
            num = num*26 + (ord(ch)-64)
        return num
        
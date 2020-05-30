class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split()
        return len(st[-1]) if len(st) > 0 else 0
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        track = {}
        for i in range(len(s)):
            if i == len(s)-1 and s[i] not in track:
                return i
            elif s[i] not in track and s[i] not in s[i+1:]:
                return i
            else:
                if s[i] not in track:
                    track[s[i]] = True
        
        return -1
        
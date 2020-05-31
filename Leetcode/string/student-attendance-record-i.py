class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = s.count('A')
        countL = s.split('LLL')
        if len(countL) > 1:
            return False
        if countA > 1:
            return False
        return True

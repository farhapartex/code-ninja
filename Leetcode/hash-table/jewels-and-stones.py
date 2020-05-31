class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        data = [True for ch in S if ch in J]
        
        return len(data)
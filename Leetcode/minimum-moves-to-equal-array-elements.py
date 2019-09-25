class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        move=0
        for n in nums:
            move += (n-mn)
        
        return move
        
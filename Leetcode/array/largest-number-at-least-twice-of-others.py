class Solution:
        
    def dominantIndex(self, nums: List[int]) -> int:
        a = max(nums)
        index = nums.index(a)
        for n in nums:
            if not a >=2*n and a!=n:
                return -1
        return index
        
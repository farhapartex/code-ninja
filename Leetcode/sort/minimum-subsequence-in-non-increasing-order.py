class Solution:
    
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums[:] = sorted(nums, reverse=True)
        value, res, total_sum = 0, [], sum(nums)
        
        for i in range(len(nums)):
            value += nums[i]
            res.append(nums[i])
            if value > total_sum-value:
                return res
        
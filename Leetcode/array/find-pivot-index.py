class Solution(object):
    
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        l = 0
        
        for i in range(0,len(nums)):
            total -= nums[i]
            if total == l:
                return i
            l += nums[i]
        
        return -1
        
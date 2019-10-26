class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        data = [min(nums[i],nums[i+1]) for i in range(0,len(nums),2)]
        return sum(data)
        
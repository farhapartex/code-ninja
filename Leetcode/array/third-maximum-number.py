class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1, max2, max3 = -1, -1, -1
        nums[:] = sorted(list(set(nums)))
       
        if len(nums) >=3 and nums[-1] != nums[-2] and nums[-2] != nums[-3]:
            return nums[-3]
        else:
            return nums[-1]
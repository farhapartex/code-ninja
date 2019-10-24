class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln, j = len(nums), 0
        if ln in[0,1]: return ln
        
        for i in range(ln-1):
            if nums[i] != nums[i+1]:
                nums[j], j = nums[i], j+1
        nums[j] = nums[-1]
        
        return j+1
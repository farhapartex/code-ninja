class Solution:
    
    def binary_search(self, nums, target):
        bg, end = 0, len(nums)-1
        
        while bg <= end:
            mid = (bg+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bg = mid+1
            else:
                end = mid-1
        
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,target)
        
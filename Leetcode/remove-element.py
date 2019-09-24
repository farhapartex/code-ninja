class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L ,j = len(nums),0
        while True:
            if j == len(nums):
                break
            if nums[j] == val:
                del nums[j]
            else:
                j+=1
            
        return len(nums)
            
        
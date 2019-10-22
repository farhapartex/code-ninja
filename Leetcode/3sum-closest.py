class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return
        nums.sort()
        diff = target - (nums[0] + nums[1] + nums[2])
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if target <=0 and nums[i] > 0:
                break
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return target
                
                new_diff = target - sum
                if abs(new_diff) < abs(diff):
                    diff = new_diff
        
        return target - diff
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        data, max_num = {}, 0
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for i in data:
            if data[i] > len(nums)//2 and max_num < data[i]:
                max_num = i
        return max_num
        
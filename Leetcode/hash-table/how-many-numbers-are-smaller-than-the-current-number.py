class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp, data = sorted(nums), {}
        for index, n in enumerate(temp):
            if n not in data:
                data[n] = len(temp[:index])
        
        return [data[n] for n in nums]
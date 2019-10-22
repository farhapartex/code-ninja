class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_one = 0, 0
        for num in nums:
            if num==1:
                count += 1
                if max_one < count:
                    max_one = count
            elif num == 0:
                    count=0
        
        return max_one
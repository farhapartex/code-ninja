from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # arr = Counter(nums)
        # arr = sorted(arr.items(), key= lambda item: item[1], reverse=True)
        # return [item[0] for item in arr if item[1]==2]
        data, res = {}, []
        for n in nums:
            if n in data:
                data[n] += 1
                res.append(n)
            else:
                data[n] = 1
        
        return res
        
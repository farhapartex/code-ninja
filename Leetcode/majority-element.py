class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        context={}
        mx, majority = 0 , 0
        for n in nums:
            if n in context:
                context[n] += 1
                if mx < context[n]:
                    mx = context[n]
                    majority = n
            else:
                context[n] = 1
                if mx == 0:
                    mx=1
                    majority = n
        return majority
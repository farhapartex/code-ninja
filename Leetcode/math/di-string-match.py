class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        nums = list(range(len(S)+1))
        data = []
        for ch in S:
            if ch == "I":
                data.append(nums.pop(0))
            else:
                data.append(nums.pop())
        data.append(nums.pop())
        return data
        
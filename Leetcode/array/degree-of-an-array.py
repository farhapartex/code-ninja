class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data_dict = {}
        for i, n in enumerate(nums):
            if n in data_dict:
                data_dict[n].append(i)
            else:
                data_dict[n] = [i]
        
        Max = max([len(data) for data in data_dict.values()])
        
        return min([(data[-1]-data[0]) for data in data_dict.values() if len(data) == Max])+1
        
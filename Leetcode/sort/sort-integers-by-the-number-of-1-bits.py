class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        data = {}
        return sorted(arr, key = lambda x: ("{0:b}".format(x).count('1'),x) )
        
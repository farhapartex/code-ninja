class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data = {}
        for n in set(arr):
            count = arr.count(n)
            data[n] = count
        
        return sorted(list(set(data.values()))) == sorted(list(data.values()))
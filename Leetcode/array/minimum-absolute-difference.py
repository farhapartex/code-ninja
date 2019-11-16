class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        k = min(j-i for i,j in zip(arr,arr[1:]))
        data = [[i,j] for i,j in zip(arr,arr[1:]) if j-i == k]
        return data
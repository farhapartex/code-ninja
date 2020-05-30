class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for index in range(len(arr)-1):
            if (arr[index]*2) in arr[index+1:]:
                return True
            elif arr[index] == (arr[index]//2)*2 and (arr[index]//2) in arr[index+1:]:
                return True
        return False
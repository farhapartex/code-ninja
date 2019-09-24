class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = -1,-1
        for idx,n in enumerate(numbers):
            idx1 = idx
            if target-n in numbers[idx+1:]:
                idx2 = numbers[idx+1:].index(target-n) + idx + 1
                break
        if idx1 >= 0 and idx2 >= 0:
            return [(idx1+1), (idx2+1)]
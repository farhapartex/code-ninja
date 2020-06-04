class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        flags = [False]*10001
        for n in A:
            if flags[n]:
                return n
            flags[n] = True
        
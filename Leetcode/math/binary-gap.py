class Solution:
    def binaryGap(self, N: int) -> int:
        num = bin(N)
        num = num[2:].strip("0")
        if len(num) == 1:
            return 0
        num = num.split("1")
        num.sort(reverse=True)
        return len(num[0]) + 1
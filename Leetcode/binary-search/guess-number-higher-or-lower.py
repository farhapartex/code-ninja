# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0:
            return 1
        bg, end = 1, n
        while bg <= end:
            mid = (bg+end)//2
            if guess(mid) == -1:
                end = mid-1
            elif guess(mid) == 1:
                bg = mid+1
            elif guess(mid) == 0:
                return mid
        
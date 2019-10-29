class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        N = N-1
        if N%2 == 0:
            return False
        else:
            return True
        
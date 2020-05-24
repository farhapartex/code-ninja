# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        beg, end, mid = 1,n,0
        
        while beg <= end:
            mid = (beg+end)//2
            if isBadVersion(mid):
                end = mid-1
            else:
                beg = mid+1
        
        return beg
        
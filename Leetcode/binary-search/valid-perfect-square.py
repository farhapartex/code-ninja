class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        mn, mx = 0, num
        
        while mn <= mx:
            mid = (mn + mx) >> 1
            r = mid * mid
            if r == num:
                return True
            else:
                if num < r:
                    mx = mid-1
                elif num > r:
                    mn = mid+1
        
        return False
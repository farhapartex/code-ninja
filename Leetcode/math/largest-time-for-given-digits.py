class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        for hr in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [hr//10, hr%10, m//10, m%10]
                tr = sorted(t)
                if A == tr:
                    return "{0}{1}:{2}{3}".format(t[0],t[1],t[2],t[3])
        
        return ""
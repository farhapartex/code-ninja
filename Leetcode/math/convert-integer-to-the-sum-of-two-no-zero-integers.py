class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for index in range(1, (n//2)+1):
            m = n-index
            if '0' in str(m) or '0' in str(index):
                continue
            break
        
        return [index, m]
        
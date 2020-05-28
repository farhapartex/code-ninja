class Solution:
    def binary_search(self, data):
        beg, end, mid = 0, len(data)-1, 0
        
        while beg<=end:
            mid = (beg+end)//2
            if data[mid] < 0:
                end = mid-1
            elif data[mid] >= 0:
                beg = mid+1
        
        return beg
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            index = self.binary_search(row)
            if index < len(row):
                res += len(row[index:])
        
        return res
        
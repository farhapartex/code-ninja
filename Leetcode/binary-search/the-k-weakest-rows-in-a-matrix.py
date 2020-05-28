class Solution:
    def binary_search(self, data):
        beg, end, mid = 0, len(data)-1, 0
        
        while beg<=end:
            mid = (beg+end)//2
            if data[mid] == 1:
                beg = mid+1
            elif data[mid] == 0:
                end = mid-1
        
        return end
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data, freq = [], {}
        for i,row in enumerate(mat):
            index = self.binary_search(row)
            if index >= 0:
                res = len(row[:index+1])
            else:
                res=0
                
            if res not in freq:
                freq[res] = [i]
                data.append(res)
            else:
                freq[res].append(i)
                
                #print(i, " ", res)
        
        data = sorted(data)
        #print(freq)
        res = []
        for d in data:
            res.extend(sorted(freq[d]))
        
        return res[:k]
            
        
        
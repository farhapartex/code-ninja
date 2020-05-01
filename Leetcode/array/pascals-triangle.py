class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        data, index = [], 0
        while index < numRows:
            if index == 0:
                data.append([1])
            elif index == 1:
                data.append([1,1])
            else:
                p, j = [1], 1
                while j < index:
                    k = data[index-1][j-1] + data[index-1][j]
                    p.append(k)
                    j += 1
                p.append(1)
                data.append(p)
            
            index += 1
        
        return data
                
        
        
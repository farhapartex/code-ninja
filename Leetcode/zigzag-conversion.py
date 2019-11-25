from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row,col = numRows,len(s)+1
        data = defaultdict(list)
        i,idx, down = 0,0, True
        if len(s)==0:
            return ""
        while True:
            if down:
                data[i].append(s[idx])
                if i == (numRows-1):
                    i -= 1
                    if i <0:
                        i=0
                    idx += 1
                    down = False
                else:
                    i +=1
                    idx +=1
            else:
                data[i].append(s[idx])
                if i ==0:
                    i += 1
                    if i == row:
                        i -=1
                    idx += 1
                    down = True
                else:
                    i -= 1
                    if i <0:
                        i=0
                    idx += 1
            
            if idx == len(s):
                break
        str = ""
        for i in range(numRows):
            str += "".join(data[i])
        
        return str
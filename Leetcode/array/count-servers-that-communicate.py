class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ver = [None] * len(grid[0])
        hor = None
        data = {}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if hor is None:
                        hor = (i,j)
                    else:
                        if hor not in data:
                            data[hor] = 1
                        if (i,j) not in data:
                            data[(i,j)] = 1
                        hor = (i,j)
                    
                    if ver[j] is None:
                        ver[j] = (i,j)
                    else:
                        if (i,j) not in data:
                            data[(i,j)] = 1
                        if ver[j] not in data:
                            data[ver[j]] = 1
                        
                        ver[j] = (i,j)
                if j == len(grid[0])-1:
                    hor = None
                    
        return len(data)
        
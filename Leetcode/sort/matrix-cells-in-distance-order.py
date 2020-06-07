class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        data = {}
        
        for r in range(R):
            for c in range(C):
                value = abs(r0-r) + abs(c0-c)
                if value not in data:
                    data[value] = [[r,c]]
                else:
                    data[value].append([r,c])
                    
        return [d for key in sorted(data.keys()) for d in data[key]]
        
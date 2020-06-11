class Solution:
        
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        def sort_mat(i, j, data):
            if i > row-1 or j > col-1:
                return sorted(data)
            
            sorted_data = sort_mat(i+1, j+1, data+[mat[i][j]])
            mat[i][j] = sorted_data[-1]
            return sorted_data[:-1]
        
        
        for j in range(col):
            sort_data = sort_mat(0, j, [])
            
        for i in range(row):
            sort_data = sort_mat(i, 0, [])
        
        
        return mat
            
            
        
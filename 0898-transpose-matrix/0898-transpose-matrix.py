class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col = len(matrix),len(matrix[0])
        new_mat = [[0 for _ in range(row) ] for _ in range(col)]

        for i in range(col):
            for j in range(row):
                new_mat[i][j] = matrix[j][i]
        return new_mat
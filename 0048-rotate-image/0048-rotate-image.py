class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        for mat in zip(*matrix[::-1]):
            matrix[i] = mat
            i+=1
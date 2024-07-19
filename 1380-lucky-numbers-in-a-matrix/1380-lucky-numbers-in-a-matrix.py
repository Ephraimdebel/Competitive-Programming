class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        for i in matrix:
            minval = min(i)
            index = i.index(minval)
            is_max_in_column = True  # Flag variable
            for j in range(len(matrix)):
                if matrix[j][index] > minval:
                    is_max_in_column = False
                    break
            if is_max_in_column:
                arr.append(minval)
        return arr
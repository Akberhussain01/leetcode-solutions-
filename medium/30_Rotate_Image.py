class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

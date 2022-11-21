class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1 # last index of matrix
        def swap(r, c):
            temp = matrix[r][c]
            matrix[r][c] = matrix[n - c][r]
            matrix[n - c][r] = matrix[n - r][n - c]
            matrix[n - r][n - c] = matrix[c][n - r]
            matrix[c][n - r] = temp

        for r in range(0, len(matrix) // 2):
            for c in range(r, len(matrix) - r - 1):
                swap(r, c)
        return matrix

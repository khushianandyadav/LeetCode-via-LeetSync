class Solution(object):

    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)

        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

        
        
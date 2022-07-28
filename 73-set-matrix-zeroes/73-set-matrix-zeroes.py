class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # two sets to hold zeros
        i_zeroes = set()
        j_zeroes = set()
        # loop through the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #if a matrix value add it to the set
                if matrix[row][col] == 0:
                    i_zeroes.add(row)
                    j_zeroes.add(col)
        #traverse the matrix again
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #if a row or column has a zero
                if row in i_zeroes or col in j_zeroes:
                    #set the row and column to zero
                    matrix[row][col] = 0
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        
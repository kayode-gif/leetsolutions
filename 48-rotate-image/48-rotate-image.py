class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #loop through row
        for i in range(len(matrix)):
            #then by every row look at the first index towards the end of col
            for j in range(i, len(matrix[0])):
                #transpose so [[1,4,7],[2,5,8],[3,6,9]]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #reverse the row 
            matrix[i] = matrix[i][::-1]
        return matrix
        """
        Do not return anything, modify matrix in-place instead.
        """
        
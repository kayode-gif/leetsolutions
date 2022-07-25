class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        #loop to build remaining rows
        for i in range(numRows - 1):
            array = [0] + ans[-1] + [0]
            newRow = []
            #look at the previous row and add 1 for extra column
            for j in range(len(ans[-1]) + 1):
                newRow.append(array[j] + array[j+1])
            ans.append(newRow)
        return ans
            
                
            
                
                
        
        
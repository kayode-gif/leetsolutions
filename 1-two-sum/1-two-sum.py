class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop through array if first number doesnt link
        for i in range(0,len(nums)):
            #loop through number after first index to find other number
            for j in range(i+1,len(nums)):
                #if the target - first == second other number
                if(target - nums[i] == nums[j]):
                    #return the index of it 
                    return [i,j]
            
                    
                
            
        
                
                
                
            
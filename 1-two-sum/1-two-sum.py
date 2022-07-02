class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #(O(N^2) Solution - inefficient)
        # result = []
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             result.append(i)
        #             result.append(j)
        # return result 
    
        #O(n) Solution
        hashMap = dict()
        for index, value in enumerate(nums):
            difference = target - value 
            if difference in hashMap:
                return [hashMap[difference],index]
            hashMap[value] = index
        return []
        
                
            
        
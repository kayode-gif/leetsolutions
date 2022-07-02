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
        #hashMap 
        hashMap = dict()
        #establish k, v of nums array
        for index, value in enumerate(nums):
            #target value - every value in array to find each difference
            difference = target - value 
            #if the remaning value is in the hashMap
            if difference in hashMap:
                #return index of hashMap value and index of other
                return [hashMap[difference],index]
            #if difference isnt in array, shift to next element 
            hashMap[value] = index
        #return empty array if target isnt acheived 
        return []
        
                
            
        
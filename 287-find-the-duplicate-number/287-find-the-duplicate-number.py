class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arrange = sorted(nums)
        #[1,2,2,3,4]
        for i in range(len(arrange)-1):
            if(arrange[i] == arrange[i+1]):
                return arrange[i]
            
            
        
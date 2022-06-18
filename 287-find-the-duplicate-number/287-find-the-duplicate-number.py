class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arrange = sorted(nums)
        #[1,2,2,3,4]
        for i in range(1,len(arrange)):
            if(arrange[i-1] == arrange[i]):
                return arrange[i]
            
            
        
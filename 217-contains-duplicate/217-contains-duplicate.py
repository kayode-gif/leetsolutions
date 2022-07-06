class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrange = sorted(nums)
        #[1,1,2,3]
        for i in range(len(arrange)-1):
            if(arrange[i] == arrange[i+1]):
                return True 
        return False
            
        
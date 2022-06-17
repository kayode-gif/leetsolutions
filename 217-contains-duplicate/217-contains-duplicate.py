class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if(len(set(nums)) == len(nums)):
                return False
            else:
                return True 
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sort = sorted(nums) #[1,1,2,3]
        for i in range(0,len(sort)-1):
            if (sort[i] == sort[i+1]):
                return True
        return False
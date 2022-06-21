class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sort = sorted(nums) #[1,2,2,3,4]
        for i in range(len(sort)):
            if(sort[i] == sort[i+1]):
                return sort[i]
        return -1
        
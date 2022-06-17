class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arrange = sorted(nums)
        for i in range(0,len(arrange)+1):
            if i not in arrange:
                return i 
        
        
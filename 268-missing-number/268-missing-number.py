class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nSet = set()
        for i in nums:
            nSet.add(i)
        for i in range(0,len(nums)+1):
            if i not in nSet:
                return i
        return 47
               
        
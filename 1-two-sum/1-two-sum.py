class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # val:index
        for i,value in enumerate(nums):
            difference = target - value
            if difference in d:
                return [d[difference],i]
            d[value] = i 
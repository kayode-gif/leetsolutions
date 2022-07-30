class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}
        for index, value in enumerate(nums):
            diff = target - value 
            if diff in hashM:
                return [hashM[diff],index]
            hashM[value] = index
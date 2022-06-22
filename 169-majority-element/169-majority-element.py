class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        for i in set(nums):
            if (nums.count(i) > len(nums) / 2) :
                return i
        return -1
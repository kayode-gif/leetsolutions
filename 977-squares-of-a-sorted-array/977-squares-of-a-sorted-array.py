class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = [nums[i]*nums[i] for i in range(len(nums))]
        arrange = sorted(square)
        return arrange
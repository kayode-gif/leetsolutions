class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        mini,maxi = 1,1 
        for i in nums:
            currMax = i*maxi
            currMin = i*mini
            maxi = max(currMax,currMin,i)
            mini = min(currMax,currMin,i)
            result = max(maxi,mini,result)
        return result 
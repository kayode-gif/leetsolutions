class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        ans = [1]*len(nums)
        #loop through for left array stuff to workout products [1,1,2,6]
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]
        #loop through right array stuff to work out products [24,12,4,1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1]*right[i+1]
        #multiply arrays to work out the products
        for i in range(0,len(nums)):
            ans[i] = left[i]*right[i]
        return ans
            
            
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set pointers to each rectangle
        left = 0
        right = len(height) - 1
        ans  = 0
        while left < right:
            #caluate max rectangle area
            ans = max(ans, (right - left) * min(height[left],height[right]))
            #keep shifting left and right dependant
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return ans
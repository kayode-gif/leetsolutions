class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0, len(letters) - 1
        if target < letters[left] or target >= letters[right]:
            return letters[left]
        while left <= right:
            m = (left+right)//2
            if letters[m] > target:
                right = m - 1
            else:
                left = m + 1 
        return letters[left]
                
        
        
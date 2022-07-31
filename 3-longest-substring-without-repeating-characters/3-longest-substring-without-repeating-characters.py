class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        longest  = 0
        right = 0
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left +=1
            charSet.add(s[right])
            longest = max(longest, len(charSet))
            right +=1 
        return longest 
                
        
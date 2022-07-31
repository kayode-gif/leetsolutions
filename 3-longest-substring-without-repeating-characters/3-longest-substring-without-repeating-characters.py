class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set pointers 
        i = 0
        j = 0
        #create set to establish no duplicates
        charSet = set()
        #returns max 
        long = 0
        while j < len(s):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            long = max(long,len(charSet))
            j +=1
        return long
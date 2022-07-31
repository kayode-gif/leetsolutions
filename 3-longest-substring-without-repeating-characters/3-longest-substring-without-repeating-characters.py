class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set pointers 
        i = 0
        j = 0
        #create set to establish no duplicates
        charSet = set()
        #returns longesr
        long = 0
        #while right most pointer < length
        while j < len(s):
            #if right most value is in set
            while s[j] in charSet:
                #remove the left most
                charSet.remove(s[i])
                #increment
                i += 1
            #keep adding right most until condition occurs and ++
            charSet.add(s[j])
            #return 
            long = max(long,len(charSet))
            j +=1
        return long
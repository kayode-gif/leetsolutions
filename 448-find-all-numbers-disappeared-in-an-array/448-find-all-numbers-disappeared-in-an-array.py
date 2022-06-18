class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #stores the missing numbers 
        arrayM = []
        numSet = set()
        #loop through if number in set add it
        for i in nums:
            numSet.add(i)
        #now loop through [1,n] if its not add it into arrayM
        for i in range(1,len(nums)+1):
            if (i not in numSet):
                arrayM.append(i)
        return arrayM
        
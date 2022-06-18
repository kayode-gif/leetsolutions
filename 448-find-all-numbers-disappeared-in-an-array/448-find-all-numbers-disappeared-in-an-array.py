class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #stores the missing numbers 
        arrayM = []
        numSet = set()
        for i in nums:
            numSet.add(i)
        for i in range(1,len(nums)+1):
            if (i not in numSet):
                arrayM.append(i)
        return arrayM
        
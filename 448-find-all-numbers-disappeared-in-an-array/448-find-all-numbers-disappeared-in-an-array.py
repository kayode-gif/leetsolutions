class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        diss = []
        numsSet = set()
        for i in nums:
            numsSet.add(i)
        for i in range(1,len(nums)+1):
            if i not in numsSet:
                diss.append(i)
        return diss
            
        
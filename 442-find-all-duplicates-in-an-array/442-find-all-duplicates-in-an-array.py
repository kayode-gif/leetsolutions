class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        array = []
        #[1,2,2,3,3,4,7,8]
        for i in range(0,len(sort)-1):
            if(sort[i] == sort[i+1]):
                array.append(sort[i])
        return array 
        
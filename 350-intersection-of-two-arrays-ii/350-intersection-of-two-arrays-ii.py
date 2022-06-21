class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fSort = sorted(nums1)
        sSort = sorted(nums2)
        ans = []
        for i in fSort:
            if i in sSort:
                ans.append(i)     
                sSort.remove(i)
        return ans
                
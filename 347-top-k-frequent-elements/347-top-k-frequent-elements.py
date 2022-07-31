class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n]+=1
        result = sorted(dic,key=dic.get,reverse = True)
        return result[:k]
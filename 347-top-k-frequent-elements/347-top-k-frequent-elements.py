class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # establish dictionary for frequency table 
        dic = {}
        # for numbers in the list
        for n in nums:
            # if we havent seen the number in the dic, set to 1
            if n not in dic:
                dic[n] = 1
            #increment the freqency 
            else:
                dic[n] +=1 
        # sort the hashmap to descend order, (key = dic.get the values)
        result = sorted(dic, key = dic.get, reverse = True)
        # return list of top elements
        return result[0:k]
        
        #heap solution
        if not nums:
            return []
        if len(nums) == k:
            return nums 
        frequency = Counter(nums) #frequency hashmap
        return heapq.nlargest(k,frequency.keys(), key = frequency.get)
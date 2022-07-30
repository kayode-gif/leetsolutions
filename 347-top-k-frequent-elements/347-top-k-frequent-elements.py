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
        
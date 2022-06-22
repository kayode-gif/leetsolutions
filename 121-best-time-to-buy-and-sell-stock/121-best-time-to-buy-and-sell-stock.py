class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# O(N^2) SOLUTION
#         profit  = 0
#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 if (prices[j] - prices[i] > profit):
#                     profit = prices[j] - prices[i]
#         return profit
                
#O(N) SOLUTION 
        #holds profit
        maxP = 0
        #set minimum buy to the first value
        buy = prices[0]
        #loop through the array looking for "current" values less than min
        for i in range(1,len(prices)):
            if(prices[i] < buy):
                #if a new minimum is found, buy it!
                buy = prices[i]
            else:
                #if a new minimum isnt, return 0 or diff between sold - min buy
                maxP = max(maxP, prices[i] - buy)
        return maxP
                
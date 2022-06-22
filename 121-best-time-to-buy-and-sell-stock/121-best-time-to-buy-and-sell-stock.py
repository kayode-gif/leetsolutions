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
        maxP = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if(prices[i] < buy):
                buy = prices[i]
            else:
                maxP = max(maxP, prices[i] - buy)
        return maxP
                
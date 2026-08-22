class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(len(prices)) :
            sell = prices[i]
            buy = min(buy, sell)
            profit = max(profit, sell - buy)
            
        return profit 
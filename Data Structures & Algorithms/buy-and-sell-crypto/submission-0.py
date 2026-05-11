class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0
        for i in range(len(prices)):
            min_p = min(min_p,prices[i])
            c_profit = prices[i] - min_p
            profit = max(c_profit,profit)
        return profit
    

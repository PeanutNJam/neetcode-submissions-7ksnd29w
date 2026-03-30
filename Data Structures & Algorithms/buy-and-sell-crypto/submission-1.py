class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(sell - minBuy, maxP)
            minBuy = min(minBuy, sell)

        return maxP

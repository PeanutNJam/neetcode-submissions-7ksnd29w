class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0

        while l < len(prices) - 1:
            for r in range(l + 1, len(prices)):
                res = max(-prices[l] + prices[r], res)
            l += 1

        return res
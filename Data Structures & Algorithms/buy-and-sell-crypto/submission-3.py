class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        res = -float("inf")
        for r in range(len(prices)):
            buy = min(prices[r], buy)
            if prices[r] > buy:
                res = max(prices[r] - buy, res)

        return res if res != -float("inf") else 0



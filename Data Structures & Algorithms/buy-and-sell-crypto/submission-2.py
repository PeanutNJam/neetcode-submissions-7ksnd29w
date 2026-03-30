class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = l = 0
        mini = prices[l]

        for r in range(1, len(prices)):
            while l < r and prices[r] < mini:
                mini = prices[r]
                l = r

            res = max(res, prices[r] - mini)

        return res
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = rest = 0

        for i in range(1, len(prices)):
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - prices[i])
            sold = max(prev_sold, prev_hold + prices[i])
            rest = max(prev_rest, prev_sold)

        return max(rest, sold)


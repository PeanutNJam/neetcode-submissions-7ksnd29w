class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        
        for j in range(len(coins) - 1, -1, -1):
            c = coins[j]
            for i in range(c, amount + 1):
                dp[i] = min(dp[i - c] + 1, dp[i])

        return dp[-1] if dp[-1] != float("inf") else -1

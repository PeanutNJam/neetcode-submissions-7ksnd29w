class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - c] if i >= c else 0

        return dp[-1]
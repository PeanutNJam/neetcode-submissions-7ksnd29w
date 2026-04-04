class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([0] * n) for _ in range(m)]

        dp[-1][-1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                elif r == m - 1:
                    dp[r][c] = dp[r][c + 1]
                elif c == n - 1:
                    dp[r][c] = dp[r + 1][c]
                elif c != n - 1:
                    dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
        print(dp)
        return dp[0][0]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[-1][-1] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if j < m and s1[j] == s3[i + j]:
                    dp[i][j] = dp[i][j + 1]
                if i < n and s2[i] == s3[i + j]:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]





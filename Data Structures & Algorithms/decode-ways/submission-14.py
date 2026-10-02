class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
            else:
                continue

            if i < n - 1 and int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]
        print(dp)
        return dp[0]
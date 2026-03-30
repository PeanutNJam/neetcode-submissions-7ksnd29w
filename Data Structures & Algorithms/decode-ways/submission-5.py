class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1 if s[0] != "0" else 0

        dp = [0] * (n + 1)
        dp[n] = 1

        second_digit = {"0", "1", "2", "3", "4", "5", "6"}

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            dp[i] = dp[i + 1]
            
            if i != n - 1 and (s[i] == "1" or (s[i] == "2" and (s[i + 1] in second_digit))):
                dp[i] += dp[i + 2]

                

        return dp[0]
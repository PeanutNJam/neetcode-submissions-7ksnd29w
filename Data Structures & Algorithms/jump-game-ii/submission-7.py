class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n - 2, -1, -1):
            add = min(n - i, nums[i])
            dp[i] = min(dp[i + 1], dp[i + add]) + 1

        return dp[0]
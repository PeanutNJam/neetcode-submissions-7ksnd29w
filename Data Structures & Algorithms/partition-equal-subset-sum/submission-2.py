class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [([False] * (target + 1)) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(n):
            for j in range(1, target + 1):
                if dp[i - 1][j] or dp[i - 1][j - nums[i]]:
                    dp[i][j] = True


        return dp[-1][-1]

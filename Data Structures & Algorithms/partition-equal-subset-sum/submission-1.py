class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False

        target = sum(nums)//2

        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(target + 1):
                if dp[i - 1][j] or dp[i - 1][j - nums[i]]:
                        dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j] 

        return dp[-1][-1]
                

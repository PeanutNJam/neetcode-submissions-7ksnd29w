class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if not n:
            return nums[0]
        if n == 1:
            return max(nums)

        first = nums[1::]
        second = nums[0:-1]

        dp1 = [0] * (n)
        dp2 = dp1.copy()
        dp1[0], dp2[0] = first[0], second[0]
        dp1[1], dp2[1] = max(first[0], first[1]), max(second[0], second[1])

        for i in range(2, n):
            dp1[i] = max(first[i] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(second[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[-1], dp2[-1])

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(2, n):
            nums[i - 1] = max(nums[i - 2], nums[i - 1])
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            

        print(nums)

        return max(nums[-1], nums[-2])
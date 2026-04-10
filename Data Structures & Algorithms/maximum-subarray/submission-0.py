class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float("inf")
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i + 1, n):
                curr += nums[j]
                if curr < 0:
                    break
                res = max(res, curr)

        return res if res != -float("inf") else -1


                

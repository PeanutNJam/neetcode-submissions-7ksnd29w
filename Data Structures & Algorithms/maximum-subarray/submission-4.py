class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float("inf")
        curr = 0
        n = len(nums)

        for i in range(n):
            curr += nums[i]
            res = max(curr, res)
            if curr < 0:
                curr = 0
            

        return res if res != -float("inf") else -1
       


                

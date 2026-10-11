class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        res = nums[0]

        for num in nums:
            curr = curMax * num
            curMax = max(num * curMin, curr, num)
            curMin = min(curMin * num, curr, num)
            res = max(curMax, res)

        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currMax = currMin = 1
        res = 0
        temp = currMax

        for num in nums:
            temp = currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num * currMin, num * temp, num)
            res = max(currMax, currMin, res)

        return res

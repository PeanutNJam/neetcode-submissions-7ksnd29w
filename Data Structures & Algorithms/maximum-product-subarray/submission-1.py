class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            tmp = num * currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp, currMin * num, num)
            res = max(currMax, res)

        return res
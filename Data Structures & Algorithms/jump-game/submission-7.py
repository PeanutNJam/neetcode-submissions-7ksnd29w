class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False

        res = nums[0]
        for i in range(1, n - 1):
            res -= 1
            if nums[i]:
                res = max(nums[i], res)
            if res <= 0 and not nums[i]:
                    return False
        
        return res > 0



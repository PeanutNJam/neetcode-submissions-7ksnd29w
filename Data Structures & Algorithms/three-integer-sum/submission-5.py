class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i and nums[i - 1] == a:
                continue

            l, r = i + 1, n - 1

            while r > l:
                total = a + nums[l] + nums[r]
                if total == 0:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res
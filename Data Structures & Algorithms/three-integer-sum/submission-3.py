class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        len_nums = len(nums)

        for i, n in enumerate(nums):
            if i and nums[i - 1] == n:
                continue

            l, r = i + 1, len_nums - 1

            while r > l:
                total = n + nums[l] + nums[r]
                if total == 0:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif total > 0:
                    r -= 1

                else:
                    l += 1

        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = 1001

        while r >= l:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            mid = l + (r-l)//2

            res = min(res, nums[mid])

            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return res


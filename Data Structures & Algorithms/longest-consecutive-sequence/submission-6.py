class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                long = 0

                while num in num_set:
                    num += 1
                    long += 1

                res = max(res, long)

        return res






        
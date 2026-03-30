class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_nums = set(nums)

        return len(set_nums) < n
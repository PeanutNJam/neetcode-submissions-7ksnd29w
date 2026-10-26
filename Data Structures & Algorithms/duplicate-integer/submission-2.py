class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            if count[num]:
                return True
            count[num] += 1

        return False
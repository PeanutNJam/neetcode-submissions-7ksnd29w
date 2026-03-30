class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(i, curr):
            now = curr.copy()
            now.append(nums[i])

            res.append(now)

            for j in range(i + 1, len(nums)):
                backtrack(j, now)

            return

        for i in range(len(nums)):
            backtrack(i, [])

        return res
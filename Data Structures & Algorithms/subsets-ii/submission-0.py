class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()

        def backtrack(i):
            if i >= len(nums):
                curr = subset.copy()
                curr_tuple = tuple(sorted(curr))
                if curr_tuple in visited:
                    return
                visited.add(curr_tuple)
                res.append(curr)
                return

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
                
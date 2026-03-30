class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total_visited = set()
        candidates.sort()

        def dfs(i, val):
            if val == target:
                visited = tuple(subset)
                if visited in total_visited:
                    return
                curr = subset.copy()
                res.append(curr)
                total_visited.add(visited)
                return
            
            if i >= len(candidates) or val > target:
                return

            subset.append(candidates[i])
            dfs(i + 1, val + candidates[i])
            subset.pop()
            dfs(i + 1, val)

        dfs(0, 0)

        return res


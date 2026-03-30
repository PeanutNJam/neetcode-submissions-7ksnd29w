class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(left, right):
            if not left and not right:
                res.append("".join(subset))
                return

            if left > 0:
                subset.append("(")
                backtrack(left - 1, right)
                subset.pop()

            if right > left:
                subset.append(")")
                backtrack(left, right - 1)
                subset.pop()

            return

        backtrack(n, n)
        return res

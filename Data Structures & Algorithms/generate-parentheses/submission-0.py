class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(left, right):
            if left == 0 and right == 0:
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

        backtrack(n, n)
        return res

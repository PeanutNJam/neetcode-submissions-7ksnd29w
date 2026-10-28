class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                nt, ni = stack.pop()
                res[ni] = i - ni

            stack.append((t, i))
        
        return res

        





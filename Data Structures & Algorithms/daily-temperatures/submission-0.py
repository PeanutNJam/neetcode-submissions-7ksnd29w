class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                curr_i, curr_t = stack.pop()
                res[curr_i] = i - curr_i
                
            stack.append((i, temp))

        return res

                
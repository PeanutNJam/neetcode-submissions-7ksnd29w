class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        total = []
        stack = []

        for i in range(n):
            total.append((position[i], speed[i]))

        total.sort(reverse=True)

        for p, s in total:
            val = (target - p) / s
            if stack and stack[-1] >= val:
                continue
            
            stack.append(val)

        return len(stack)



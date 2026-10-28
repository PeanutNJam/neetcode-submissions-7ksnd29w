class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vals = sorted(zip(position, speed))

        stack = []

        for p, s in vals[::-1]:
            val = (target - p) / s
            
            if stack and val <= stack[-1]:
                continue

            stack.append(val)

        return len(stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = {"+", "-", "/", "*"}

        res = 0
        stack = []

        for char in tokens:
            if not stack:
                stack.append(int(char))
            else:
                if char in signs:
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    if char == "+":
                        curr = second_pop + first_pop
                    elif char == "-":
                        curr = second_pop - first_pop
                    elif char == "/":
                        curr = int(float(second_pop) / first_pop)
                    else:
                        curr = second_pop * first_pop
                    stack.append(curr)
                else:
                    stack.append(int(char))

        return stack[-1]

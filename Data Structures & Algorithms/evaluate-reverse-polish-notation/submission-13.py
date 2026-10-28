class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(second + first)
            elif char == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif char == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(second * first)
            elif char == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(float(second / first)))
            else:
                stack.append(int(char))

        return stack[0]

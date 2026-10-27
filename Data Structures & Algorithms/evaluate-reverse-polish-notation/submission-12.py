class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0
        signs = ("+", "-", "*", "/")

        for char in tokens:
            if char in signs:
                first = int(stack.pop())
                second = int(stack.pop())
                if char == "+":
                    stack.append(first + second)
                elif char == "-":
                    stack.append(second - first)
                elif char == "*":
                    stack.append(first * second)
                else:
                    val = second/first
                    if val <= 0:
                        stack.append(math.ceil(second/first))
                    else:
                        stack.append(math.floor(second/first))
            else:
                stack.append(char)
        return int(stack[0])
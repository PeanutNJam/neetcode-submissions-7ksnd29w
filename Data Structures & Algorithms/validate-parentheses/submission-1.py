class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if stack and ((char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{")):
                stack.pop()
            else:
                stack.append(char)

        return not stack
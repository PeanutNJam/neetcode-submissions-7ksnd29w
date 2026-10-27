class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c not in parent_map:
                stack.append(c)
            else:
                if stack and stack[-1] == parent_map[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

        
                

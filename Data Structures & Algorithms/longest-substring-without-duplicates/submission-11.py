class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            res = max(r - l + 1, res)

        return res

            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = res = 0

        while l < n:
            chars = set()
            count = 0
            for r in range(l, n):
                if s[r] in chars:
                    break
                count += 1
                chars.add(s[r])
                res = max(res, count)
            l += 1

        return res


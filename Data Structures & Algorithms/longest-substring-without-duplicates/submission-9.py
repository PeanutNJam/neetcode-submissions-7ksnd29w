class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        included = set()

        l = res = 0
        n = len(s)

        for r in range(n):
            while s[r] in included:
                included.remove(s[l])
                l += 1
            included.add(s[r])
            res = max(res, r - l + 1)
        return res
                
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = l = maxFreq = 0

        for r in range(len(s)):
            count[s[r]] += 1
            curr = count[s[r]]
            maxFreq = max(maxFreq, curr)

            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


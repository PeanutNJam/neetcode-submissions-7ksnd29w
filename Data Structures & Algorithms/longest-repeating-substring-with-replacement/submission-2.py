class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxFreq = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            curr_count = count[s[r]]
            maxFreq = max(curr_count, maxFreq)

            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

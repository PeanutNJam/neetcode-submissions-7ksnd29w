class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        s_count = defaultdict(int)
        l = 0

        for char in t:
            t_count[char] += 1

        res, resLength = [-1, -1], float("infinity")
        currCount, tCount = 0, len(t_count)

        for r in range(len(s)):
            s_count[s[r]] += 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                currCount += 1

            while currCount == tCount:
                if r - l + 1 < resLength:
                    res = [l, r + 1]
                    resLength = r - l + 1
                s_count[s[l]] -= 1
                if s_count[s[l]] < t_count[s[l]] and s[l] in t_count:
                    currCount -= 1
                l += 1

        return s[res[0]:res[1]]



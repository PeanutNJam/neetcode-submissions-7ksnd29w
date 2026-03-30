class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for char in t:
            t_count[char] += 1

        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(t_count)
        l = 0

        for r in range(len(s)):
            s_count[s[r]] += 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1
                s_count[s[l]] -= 1

                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        return s[res[0]: res[1]]





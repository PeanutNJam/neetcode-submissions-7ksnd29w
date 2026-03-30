class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        window_count = defaultdict(int)
        curr = total = l = 0

        res = [0, 0]
        resLen = float("inf")

        for char in t:
            t_count[char] += 1
            total += 1

        for r in range(len(s)):
            c = s[r]
            window_count[c] += 1

            if c in t_count and window_count[c] <= t_count[c]:
                curr += 1

            while curr == total:
                curr_len = r - l + 1
                if curr_len < resLen:
                    resLen = curr_len
                    res = [l, r]


                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    curr -= 1

                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        res_count = float("inf")

        t_count = Counter(t)
        have, need = 0, len(t_count)
        curr_count = defaultdict(int)
        
        for r in range(len(s)):
            curr_count[s[r]] += 1
            if s[r] in t_count and curr_count[s[r]] == t_count[s[r]]:
                have += 1

            while need == have and r >= l:
                if res == "":
                    res = s[l: r + 1]
                elif res_count > r - l + 1:
                    res_count = r - l + 1
                    res = s[l: r + 1]
                curr_count[s[l]] -= 1
                if s[l] in t_count and curr_count[s[l]] + 1 == t_count[s[l]]:
                    have -= 1
                l += 1

        return res
                



            
                

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        res_count = float("inf")

        t_map = defaultdict(int)
        curr_count = defaultdict(int)
        for char in t:
            t_map[char] += 1

        have, need = 0, len(t_map)

        for r in range(len(s)):
            c = s[r]
            curr_count[c] += 1

            if curr_count[c] == t_map[c]:
                have += 1

            while have == need:
                if r - l + 1 < res_count:
                    res = s[l : r + 1]
                    res_count = r - l + 1
                
                curr_count[s[l]] -= 1

                if curr_count[s[l]] < t_map[s[l]]:
                    have -= 1
                
                l += 1



        return res
            
                

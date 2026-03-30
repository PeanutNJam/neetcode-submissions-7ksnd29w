from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        window = defaultdict(int)
        have, need = 0, len(t_map)
        res = ""
        res_len = float("inf")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if window[c] == t_map[c]:
                have += 1
            
            # shrink window
            while have == need:
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                
                l += 1
        
        return res
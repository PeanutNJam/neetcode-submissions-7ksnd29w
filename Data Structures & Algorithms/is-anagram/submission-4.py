class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        s_count, t_count = defaultdict(int), defaultdict(int)

        for i in range(n):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        return s_count == t_count




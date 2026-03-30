class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        max_count = count = 0
        for c in s1:
            s1_count[c] += 1

        l = 0
        for r in range(len(s2)):
            s2_count[s2[r]] += 1
            count += 1
            while s2_count[s2[r]] > s1_count[s2[r]]:
                s2_count[s2[l]] -= 1
                l += 1
                count -= 1
            max_count = max(max_count, count)

            
        return max_count == len_s1

            

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l = 0

        for r in range(len(s2)):
            count[s2[r]] -= 1

            if r - l + 1 > len(s1):
                count[s2[l]] += 1
                l += 1

            if all(v == 0 for v in count.values()):
                return True

        return False
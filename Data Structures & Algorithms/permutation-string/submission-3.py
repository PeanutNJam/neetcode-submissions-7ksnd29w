class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = Counter(s1)
        refer = count.copy()

        for idx in range(len(s2)):
            r = idx
            while r < len(s2) and count[s2[r]] > 0:
                count[s2[r]] -= 1
                l += 1
                r += 1
            
            print(l)
            if l == len(s1):
                return True
            else:
                l = 0
                count = refer.copy()

        return False

            
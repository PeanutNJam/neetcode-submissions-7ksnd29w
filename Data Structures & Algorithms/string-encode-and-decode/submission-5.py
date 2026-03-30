class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = j = 0

        while i < n:
            if s[j] == "#":
                count = int(s[i : j])
                i = j + 1
                j += count + 1
                res.append(s[i : j])
                i = j
            else:
                j += 1

        return res

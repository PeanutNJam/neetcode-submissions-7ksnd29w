class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = defaultdict(list)
        res = []

        for s in strs:
            s_dict["".join(sorted(list(s)))].append(s)

        for val in s_dict.values():
            res.append(val)

        return res
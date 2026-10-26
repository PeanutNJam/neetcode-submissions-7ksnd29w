class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val_map = defaultdict(list)
        for s in strs:
            val_map["".join(sorted(s))].append(s)

        res = []
        for item in val_map.values():
            res.append(item)

        return res



        



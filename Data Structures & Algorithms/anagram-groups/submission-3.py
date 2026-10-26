class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val_map = defaultdict(list)
        for s in strs:
            char = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                char[idx] += 1
            val_map[tuple(char)].append(s)

        return list(val_map.values())
            


        



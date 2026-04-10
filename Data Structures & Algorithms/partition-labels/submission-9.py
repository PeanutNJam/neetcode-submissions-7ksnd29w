class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_map = defaultdict(lambda: float("inf"))
        last_map = defaultdict(int)
        n = len(s)

        for i in range(n):
            char = s[i]
            first_map[char] = min(first_map[char], i)
            last_map[char] = max(last_map[char], i)

        intervals = []
        for k in first_map.keys():
            intervals.append((first_map[k], last_map[k]))

        intervals.sort()
        
        res = []
        curr_min = intervals[0][0]
        curr_max = intervals[0][1]
        for j in range(1, len(intervals)):
            if intervals[j][0] > curr_max:
                res.append(curr_max - curr_min + 1)
                curr_min = intervals[j][0]
            curr_max = max(curr_max, intervals[j][1])

        res.append(curr_max - curr_min + 1)
        return res

            




class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        if timestamp < self.dic[key][0][1]:
            return ""
        l, r = 0, len(self.dic[key]) - 1

        while r >= l:
            mid = l + (r - l) // 2

            if self.dic[key][mid][1] == timestamp:
                return self.dic[key][mid][0]

            if self.dic[key][mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        

        return self.dic[key][r][0]



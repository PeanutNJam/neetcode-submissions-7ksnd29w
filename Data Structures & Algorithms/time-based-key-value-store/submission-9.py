class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key] or self.time_map[key][0][0] > timestamp:
            return ""

        l, r = 0, len(self.time_map[key]) - 1
        while r >= l:
            mid = l + (r - l)// 2

            if self.time_map[key][mid][0] == timestamp:
                return self.time_map[key][mid][1]
            
            if timestamp > self.time_map[key][mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        if self.time_map[key][mid][0] < timestamp:
            return self.time_map[key][mid][1]
        else:
            return self.time_map[key][mid - 1][1]
        

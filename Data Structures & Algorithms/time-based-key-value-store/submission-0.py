class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        store = self.hashmap[key]
        
        if not store:
            return ""

        l, r = 0, len(store) - 1
        res = ""

        while l <= r:
            mid = l + (r - l) // 2
            mid_timestamp = store[mid][0]
            
            if mid_timestamp == timestamp:
                return store[mid][1]
            elif mid_timestamp < timestamp:
                res = store[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
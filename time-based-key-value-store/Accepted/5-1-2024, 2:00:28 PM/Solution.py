// https://leetcode.com/problems/time-based-key-value-store

class TimeMap:

    def __init__(self):
        self.map = {} # (key, time) : value
        self.key_stamp = {} # key: [time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value
        
        if key in self.key_stamp:
            self.key_stamp[key].append(timestamp)
        else:
            self.key_stamp[key] = [timestamp]


    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.map:
            return self.map[(key, timestamp)]
        
        if key not in self.key_stamp:
            return ""
        stamps = self.key_stamp[key]

        l = 0
        r = len(stamps)-1
        if stamps[r] < timestamp:
            return self.map[(key, stamps[r])]
        elif stamps[0] > timestamp:
            return ""

        while l <= r:
            if l==r:
                return self.map[(key, stamps[l])]
            
            mid = ceil((l+r)/2)

            if stamps[mid] == timestamp:
                return self.map[(key, stamps[mid])]
            elif stamps[mid] < timestamp:
                l = mid
            elif stamps[mid] > timestamp:
                r = mid-1

        
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
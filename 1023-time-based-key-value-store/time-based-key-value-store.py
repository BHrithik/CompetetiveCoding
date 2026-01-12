class TimeMap:
    def find_last(self, values, time):
        l = 0
        r = len(values)-1
        latest_time = values[0][0]
        latest_value = ""
        while l <= r:
            m = (l+r)//2
            if values[m][0] == time:
                return values[m][1]
            if time < values[m][0]:
                r = m-1
            elif time > values[m][0]:
                latest_time = values[m][0]
                latest_value = values[m][1]
                l = m+1
        return latest_value


    def __init__(self):
        self.my_dict = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_dict:
            self.my_dict[key].append((timestamp,value))
        else:
            self.my_dict[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.my_dict:
            values = self.my_dict[key]
            return self.find_last(values,timestamp)
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
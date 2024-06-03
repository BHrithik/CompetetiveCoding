class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if not key in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            val = self.values[self.keys.index(key)]
            if val is not None:
                return self.values[self.keys.index(key)]
            else:
                return -1
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.values[self.keys.index(key)] = None
        else:
            return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
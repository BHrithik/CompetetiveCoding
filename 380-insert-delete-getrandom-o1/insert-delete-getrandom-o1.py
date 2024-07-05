class RandomizedSet:

    def __init__(self):
        self.hashMap = set()

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        else:            
            self.hashMap.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            self.hashMap.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        num = random.randrange(0,len(self.hashMap))
        return list(self.hashMap)[num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
from collections import OrderedDict, Counter

class FirstUnique:
    def __init__(self, nums):
        self.data = OrderedDict()
        self.counts = Counter(nums)
        for num in nums:
            if self.counts[num] == 1:
                self.data[num] = None

    def showFirstUnique(self):
        if self.data:
            return next(iter(self.data))
        return -1

    def add(self, value):
        if value in self.counts:
            if self.counts[value] == 1:
                self.data.pop(value, None)
            self.counts[value] += 1
        else:
            self.counts[value] = 1
            self.data[value] = None

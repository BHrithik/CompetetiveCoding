class TwoSum:

    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        self.arr.sort()
        l = 0
        r = len(self.arr)-1
        while l < r:
            if self.arr[l]+self.arr[r] == value:
                return True
            elif self.arr[l]+self.arr[r] > value:
                r -= 1
            else:
                l += 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        start = 0
        k = k - 1
        for i in range(0, n):
            arr.append(i)
        for i in range(n - 1):
            to_be_popped = (start + k) % len(arr)
            print(f"Removed member {arr[to_be_popped]}")
            arr.pop(to_be_popped)
            start = to_be_popped % len(arr)
        return arr[0]+1
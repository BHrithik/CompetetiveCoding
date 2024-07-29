class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))  # Initialize the array with numbers from 1 to n
        start = 0
        k = k - 1  # We use zero-based indexing
        while len(arr) > 1:
            to_be_popped = (start + k) % len(arr)  # Find the index to be removed
            print(f"Removed member {arr[to_be_popped]}")
            arr.pop(to_be_popped)  # Remove the member
            start = to_be_popped % len(arr)  # Update start index
        return arr[0]  # Return the last remaining member
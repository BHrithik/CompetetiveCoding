class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = defaultdict(lambda: -1)
        for index, value in enumerate(nums):
            n[value] = index
        return n[target]
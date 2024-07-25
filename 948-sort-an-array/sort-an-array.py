class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Find the minimum and maximum values in the input array
        min_val, max_val = min(nums), max(nums)

        # Create buckets with a size large enough to accommodate all possible values
        n = len(nums)
        buckets = [[] for _ in range(max_val - min_val + 1)]

        # Distribute the elements into the buckets
        for num in nums:
            index = num - min_val
            buckets[index].append(num)

        # Concatenate the sorted buckets into the result
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result
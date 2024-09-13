class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        res = []
        for left, right in queries:
            if left == 0:
                res.append(prefix[right])
            else:
                res.append(prefix[right] ^ prefix[left - 1])
        return res
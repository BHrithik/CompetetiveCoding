class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        return [i for i in arr if Counter(arr)[i] == 1][k-1] if len([i for i in arr if Counter(arr)[i] == 1]) >= k else ""
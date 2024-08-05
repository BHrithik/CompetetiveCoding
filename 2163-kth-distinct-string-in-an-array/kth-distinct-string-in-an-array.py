class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a=[i for i in arr if Counter(arr)[i] == 1]
        return a[k-1] if len(a) >= k else ""
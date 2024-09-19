class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        return sorted(num_dict.keys(),key=lambda x: num_dict[x],reverse=True)[:k]
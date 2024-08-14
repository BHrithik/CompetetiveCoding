class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).keys(),key=lambda x: Counter(nums)[x],reverse=True)[0]
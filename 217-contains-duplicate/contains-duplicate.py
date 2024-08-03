class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pos_seen = 0
        neg_seen = 0
        for i in nums:
            cur_mask = 1 << abs(i)
            if i >= 0:
                if pos_seen & cur_mask:
                    return True
                else:
                    pos_seen ^= cur_mask
            else:
                if neg_seen & cur_mask:
                    return True
                else:
                    neg_seen ^= cur_mask
        return False
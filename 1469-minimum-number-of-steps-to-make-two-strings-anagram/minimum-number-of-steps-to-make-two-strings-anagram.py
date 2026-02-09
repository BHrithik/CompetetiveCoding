class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = Counter(s)
        t_dict = Counter(t)
        # we know the length of s and t are the same
        # basically need to check what we have and what we don't we need to get everything we don't have by changing
        not_have = 0
        for ch in s_dict:
            if ch not in t_dict:
                not_have += s_dict[ch]
            elif t_dict[ch] < s_dict[ch]:
                not_have += s_dict[ch]-t_dict[ch]
        return not_have
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window = len(s1)
        l = 0
        combo_dict = Counter(s1)
        char_dict = {}
        for r in range(0,len(s2)):
            char_dict[s2[r]] = char_dict.get(s2[r],0) + 1
            if r-l+1 > window:
                char_dict[s2[l]] -= 1
                if char_dict[s2[l]] == 0:
                    char_dict.pop(s2[l])
                l = l+1
            if char_dict == combo_dict:
                return True
        return False
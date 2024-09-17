class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split(" ")
        s1_dict = Counter(words_s1)
        words_s2 = s2.split(" ")
        s2_dict = Counter(words_s2)
        res = []
        for i in s1_dict:
            if s1_dict[i] == 1 and i not in s2_dict:
                res.append(i)
        for i in s2_dict:
            if s2_dict[i] == 1 and i not in s1_dict:
                res.append(i)
        return res

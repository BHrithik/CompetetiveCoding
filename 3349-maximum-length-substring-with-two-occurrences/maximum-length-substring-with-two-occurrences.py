class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        j = 0
        for i in range(len(s)):
            l_dict = defaultdict(int)
            j = i
            while j<len(s):
                l_dict[s[j]] += 1
                if l_dict[s[j]]>2:
                    break
                max_len = max(max_len,j-i+1)
                j = j+1
        return max_len
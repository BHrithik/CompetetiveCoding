class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [x for x in s.split(' ') if x]
        return ' '.join(arr[::-1])
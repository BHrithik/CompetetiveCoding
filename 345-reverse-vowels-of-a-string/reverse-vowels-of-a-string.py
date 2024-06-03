class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in 'aeiouAEIOU']
        ans = ''
        for i in s:
            if i in 'aeiouAEIOU':
                ans += vowels.pop()
            else:
                ans += i
        return ans

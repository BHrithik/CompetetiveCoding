class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalpha():
                new_s += i.lower()
            elif i.isdigit():
                new_s += i
        return new_s == new_s[::-1]
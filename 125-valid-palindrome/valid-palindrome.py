class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l < r:
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif not s[l].isdigit() and not s[l].isalpha(): ## l special character
                l += 1
            elif not s[r].isdigit() and not s[r].isalpha(): ## r special character
                r -= 1
            else:
                return False
        return True
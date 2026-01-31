class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res_dif = float('inf')
        res = ""
        for letter in letters:
            diff = ord(letter)-ord(target)
            if letter != target and diff > 0 and res_dif > diff:
                res = letter
                res_dif = ord(letter)-ord(target)
        return res if res != "" else letters[0]
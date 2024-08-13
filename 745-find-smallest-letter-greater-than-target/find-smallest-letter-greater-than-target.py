class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in letters:
            if i != target and i > target:
                return i
        return letters[0]
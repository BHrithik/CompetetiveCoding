class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bar = set(allowed)
        def checkIfAllowed(word):
            for char in word:
                if char in bar:
                    continue
                else:
                    return False
            return True
        c = 0
        for word in words:
            if checkIfAllowed(word):
                c+=1
        return c

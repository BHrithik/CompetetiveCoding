class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                if b_count > 0:
                    deletions += 1
                    b_count -= 1
        return deletions
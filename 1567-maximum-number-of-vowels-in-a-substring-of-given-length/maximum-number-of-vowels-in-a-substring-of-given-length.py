class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur_sum = sum([1 if i in "AEIOUaeiou" else 0 for i in s[:k] ])
        max_sum = cur_sum
        print(cur_sum)
        for i in range(len(s)-k):
            if s[i] not in "AEIOUaeiou" and s[i+k] in "AEIOUaeiou":
                cur_sum = cur_sum + 1
            if s[i] in "AEIOUaeiou" and s[i+k] not in "AEIOUaeiou":
                cur_sum = cur_sum - 1
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum

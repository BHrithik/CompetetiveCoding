class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCurrentCandies = max(candies)
        if extraCandies+min(candies) > maxCurrentCandies:
            return [True]*len(candies)
        ans = [True if i+extraCandies>=maxCurrentCandies else False for i in candies]
        return ans
        

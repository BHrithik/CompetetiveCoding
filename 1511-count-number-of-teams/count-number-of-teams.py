class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        for i in range(1, len(rating)-1):
            less_in_left = more_in_left = more_in_right = less_in_right = 0
            for j in range(0,i):
                if rating[j] < rating[i]:
                    less_in_left += 1
                else:
                    more_in_left += 1
            for k in range(i+1,len(rating)):
                if rating[i] < rating[k]:
                    more_in_right += 1
                else:
                    less_in_right += 1
            teams += (less_in_left*more_in_right) + (more_in_left*less_in_right)
        return teams
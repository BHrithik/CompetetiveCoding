class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i in range(0,len(seats)):
            ans = ans + abs(seats[i] - students[i])
        return ans
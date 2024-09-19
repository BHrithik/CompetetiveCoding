class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToNum(time):
            nums = time.split(":")
            return int(nums[0])*60 + int(nums[1])        
        bucket = [False]*1440
        first_t = 1441
        last_t = 0
        for time in timePoints:
            mins = timeToNum(time)
            if bucket[mins]:
                return 0
            bucket[mins] = True
            first_t = min(first_t,mins)
            last_t = max(last_t,mins)
        min_diff = 1440-last_t+first_t
        prev = first_t
        for i in range(first_t+1,len(bucket)):
            if bucket[i]:
                min_diff = min(min_diff, i-prev)
                prev = i
        return min_diff
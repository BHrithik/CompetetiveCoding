class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        def helper(i,j,k):
            a = arr[i:j]
            b = arr[j:k+1]
            ansA = 0
            ansB = 0
            for i in a:
                ansA = ansA ^ i
            for j in b:
                ansB = ansB ^ j
            if ansA == ansB:
                return True
        count = 0
        ans = []
        for i in range(len(arr)-1):
            a = 0
            for j in range(i+1,len(arr)):
                a ^= arr[j-1]
                b = 0
                for k in range(j,len(arr)):
                    b ^= arr[k]
                    if a == b:
                        count +=1
        return count
        
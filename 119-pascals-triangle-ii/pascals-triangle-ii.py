class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(0,rowIndex):
            nexVal = [0]*(len(res)+1)
            for j in range(len(res)):
                nexVal[j] += res[j]
                nexVal[j+1] += res[j]
            res = nexVal
        return res

#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
#1 5 10 10 5 1
#1 6 15 20 15 6 1
#1 7 21 25 25 21 7 1
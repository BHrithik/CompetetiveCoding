class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dfs(u,d):           #number of tiles used up in the up and down row
            if u==d==n:         #up and down rows completely filled with dominos (we assume no empty spaces because when we made recursive calls we filled only the domino or tromino which will not leave spaces)
                return 1
            elif u>n or d>n:    #tiles occupying more than n
                return 0
            count=0
            if u==d:
                count+=dfs(u+1, d+1)        #u can put straight domino
                count+=dfs(u+2, d+2)        #u can put flat domino on up + flat domino on down
                count+=dfs(u+2, d+1)        #u can put tromino with longer edge on up
                count+=dfs(u+1, d+2)        #u can put tromino with longer edge on down
            elif u<d:
                count+=dfs(u+2,d)           #u can put flat domino on up
                count+=dfs(u+2,d+1)         #u can put tromino with longer edge on up
            elif u>d:
                count+=dfs(u,d+2)           #u can put flat domino on down
                count+=dfs(u+1,d+2)         #u can put tromino longer edge on down
            return count%(10**9+7)
        return dfs(0,0)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        flowBackA,flowBackP = set(), set()
        coastA, coastP = [], []
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j, isPacific):
            if isPacific and (i,j) in flowBackP: return
            if not isPacific and (i,j) in flowBackA:return
            if isPacific: flowBackP.add((i,j))
            else: flowBackA.add((i,j))
            for di,dj in directions:
                ni,nj = i+di, j+dj
                if ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS or heights[ni][nj] < heights[i][j]:
                    continue
                dfs(ni,nj,isPacific)
        for i in range(0,ROWS):
            dfs(i,COLS-1,False)
            dfs(i,0,True)
        for i in range(0,COLS):
            dfs(ROWS-1,i,False)
            dfs(0,i,True)
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in flowBackP and (i,j) in flowBackA:
                    res.append([i,j])
        return res



        # res = set()
        # visited_p = {}
        # visited_a = {}
        # directions = [(0,1),(1,0),(-1,0),(0,-1)]
        # def dps(i, j):
        #     if i <= 0 or j <= 0:
        #         return True
        #     if i >= len(heights)-1 or j >= len(heights[0])-1:
        #         return False
        #     if (i,j) in visited_p:
        #         return visited_p[(i,j)]
        #     res = False
        #     for di,dj in directions:
        #         if heights[i+di][j+dj] <= heights[i][j]:
        #             res = res or dps(i+di,j+dj)
        #     visited_p[(i,j)]=res
        #     return visited_p[(i,j)]
                        
        # def das(i, j):
        #     if i >= len(heights)-1 or j >= len(heights[0])-1:
        #         return True
        #     if i <= 0 or j <= 0:
        #         return False
        #     if (i,j) in visited_a:
        #         return visited_a[(i,j)]
        #     res = False
        #     for di,dj in directions:
        #         if heights[i+di][j+dj] <= heights[i][j]:
        #             res = res or dps(i+di,j+dj)
        #     visited_a[(i,j)]=res
        #     return visited_a[(i,j)]

        # for i in range(0,len(heights)):
        #     for j in range(0,len(heights[i])):
        #         if dps(i,j) and das(i,j):
        #             res.add((i,j))
        # return sorted(list(res))
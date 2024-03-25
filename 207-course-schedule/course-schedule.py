class Solution:
    def canFinish(self, numCourses: int, preQ: List[List[int]]) -> bool:
        adjArr = defaultdict(list)
        for i in preQ:
            adjArr[i[0]].append(i[1])
        print(adjArr)
        visitSet = set()
        print("DFS")
        def dfs(crs):
            if crs in visitSet:
                return False
            if adjArr[crs] == []:
                return True
            visitSet.add(crs)
            for i in adjArr[crs]:
                if not dfs(i):
                    return False
            visitSet.remove(crs)
            adjArr[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
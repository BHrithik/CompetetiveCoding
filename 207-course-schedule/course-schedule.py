class Solution:
    def canFinish(self, numCourses: int, preQ: List[List[int]]) -> bool:
        courseDict = {}
        for c1,c2 in preQ:
            if c1 not in courseDict:
                courseDict[c1] = []
            courseDict[c1].append(c2)
        visited = [0]*numCourses
        def isCycle(course):
            if course not in courseDict or visited[course] == 2:
                return False
            if visited[course] == 1:
                return True
            visited[course] = 1
            for pre in courseDict[course]:
                if isCycle(pre):
                    return True
            visited[course] = 2
            return False
        for course in range(numCourses):
            if isCycle(course):
                return False
        return True









        # adjArr = defaultdict(list)
        # for i in :
        #     adjArr[i[0]].append(i[1])
        # print(adjArr)
        # visitSet = set()
        # print("DFS")
        # def dfs(crs):
        #     if crs in visitSet:
        #         return False
        #     if adjArr[crs] == []:
        #         return True
        #     visitSet.add(crs)
        #     for i in adjArr[crs]:
        #         if not dfs(i):
        #             return False
        #     visitSet.remove(crs)
        #     adjArr[crs] = []
        #     return True
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True
class Solution:
    def findOrder(self, numCourses: int, preq: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for a,b in preq:
            graph[a].append(b)
        visited = [0]*numCourses # 0 is not visited 1 is visiting 2 is visited
        outPut = []
        def isCycle(i):
            if visited[i] == 2:
                return False
            if visited[i] == 1:
                return True
            visited[i] = 1 # Visiting
            for pres in graph[i]:
                if isCycle(pres):
                    return True
            visited[i] = 2
            outPut.append(i)
            return False

        for i in range(numCourses):
            if visited[i] != 2 and isCycle(i):
                return []
        return outPut












        # courseDict = {i:[] for i in range(numCourses)}
        # for c1,c2 in preq:
        #     courseDict[c1].append(c2)
        # visited = set()
        # cycle = set()
        # output = []
        # def dfs(c):
        #     if c in cycle:
        #         return False
        #     if c in visited:
        #         return True
        #     cycle.add(c)
        #     visited.add(c)
        #     for pre in courseDict[c]:
        #         if not dfs(pre):
        #             return False
        #     cycle.remove(c)
        #     output.append(c)
        #     return True
        # for i in range(numCourses):
        #     if not dfs(i):
        #         print(output)
        #         return []
        # return output

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i:[] for i in range(numCourses)}
        for cor, pre in prerequisites:
            preqs[cor].append(pre)
        cycle, visit = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preqs[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for course in range(numCourses-1,-1,-1):
            if not dfs(course):
                return []
        return output
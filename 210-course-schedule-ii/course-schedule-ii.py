class Solution:
    def findOrder(self, numCourses: int, preq: List[List[int]]) -> List[int]:
        courseDict = {i:[] for i in range(numCourses)}
        courses = range(numCourses)
        for c1,c2 in preq:
            courseDict[c1].append(c2)
        # courses = list(courses)
        # courses.sort(key=lambda x: len(courseDict.get(x,[])))
        visited = set()
        cycle = set()
        output = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            visited.add(c)
            for pre in courseDict[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            output.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisions = defaultdict(dict)
        cur_chars = set()
        for i in range(len(values)):
            num,denominator = equations[i][0], equations[i][1]
            divisions[num][denominator] = values[i]
            divisions[denominator][num] = 1/values[i]
            cur_chars.add(num)
            cur_chars.add(denominator)
        def finVal(i, j, visited):
            if i not in divisions or j not in divisions:
                return -1.0
            if j in divisions[i]:
                return divisions[i][j]
            visited.add(i)
            for neighbor in divisions[i]:
                if neighbor not in visited:
                    temp = finVal(neighbor, j, visited)
                    if temp != -1.0:
                        divisions[i][j] = divisions[i][neighbor] * temp
                        return divisions[i][j]
            return -1.0
        results = []
        for i,j in queries:
            val = finVal(i,j,set())
            if val != -1.0:
                divisions[i][j] = val
                divisions[j][i] = 1/val
            results.append(val)
        return results
        
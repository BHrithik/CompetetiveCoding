class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        alphabets = list(set(original+changed+list(source)+list(target)))
        alphabets.sort()
        n = len(alphabets)
        matrix = [[float('inf')]*n for _ in range(n)]
        char_to_index = {char: idx for idx, char in enumerate(alphabets)}
        for i in range(len(cost)):
            o = char_to_index[original[i]]
            c = char_to_index[changed[i]]
            matrix[o][c] = min(matrix[o][c], cost[i])
        print(matrix)
        for i in range(n):
            matrix[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        total_cost = 0
        for i in range(len(source)):
            s_i = char_to_index[source[i]]
            t_i = char_to_index[target[i]]
            if matrix[s_i][t_i] == float('inf'):
                return -1
            total_cost += matrix[s_i][t_i]
        return total_cost
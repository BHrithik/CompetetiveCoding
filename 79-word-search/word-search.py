class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        b = len(board[0])
        matrix = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                matrix[board[i][j]].append((i,j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def helper(i,j,rem_word,paths):
            if rem_word == "":
                return True
            for di,dj in directions:
                ni,nj = i+di, j+dj
                if 0 <= ni < l and 0 <= nj < b:
                    if board[ni][nj] == rem_word[0] and (ni,nj) not in paths and helper(ni,nj,rem_word[1:],paths|{(ni,nj)}):
                        return True
            return False

        for i,j in matrix[word[0]]:
            if helper(i,j,word[1:],{(i,j)}):
                return True
        return False
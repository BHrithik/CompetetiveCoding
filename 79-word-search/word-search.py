class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def search(i,j,index,word):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in visited or board[i][j] != word[index]:
                return False
            if index == len(word)-1:
                return True # found complete string
            visited.add((i,j))
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for di,dj in directions:
                if search(i+di,j+dj,index+1,word):
                    return True
            visited.remove((i,j))

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,0,word):
                        return True
        return False
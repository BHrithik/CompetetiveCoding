class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isWord = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        res = set()

        def dfs(r,c,root,word,visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in root.children or (r,c) in visited:
                return
            visited.add((r,c))
            root = root.children[board[r][c]]
            word = word + board[r][c]
            if root.isWord:
                res.add(word)
            dfs(r+1,c,root,word,visited)
            dfs(r,c+1,root,word,visited)
            dfs(r-1,c,root,word,visited)
            dfs(r,c-1,root,word,visited)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"",set())
        return list(res)

        # letterdict = defaultdict(list)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         letterdict[board[i][j]].append((i,j))
        # cache = {}
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # def helper(i,j,word,paths):
        #     if word == "":
        #         return True
        #     if word in cache:
        #         l1 = len(paths)
        #         l2 = len(cache[word])
        #         if l1+l2 == len(paths|cache[word]):
        #             return True
        #     for di,dj in directions:
        #         if 0 <= i+di <len(board) and 0 <= j+dj < len(board[0]):
        #             if board[i+di][j+dj] == word[0] and (i+di, j+dj) not in paths:
        #                 if helper(i+di, j+dj, word[1:], paths | {(i+di, j+dj)}):
        #                     cache[word]=paths
        #                     return True
        #     cache[(i, j, word)] = False
        #     return False
        # result = []
        # for word in words:
        #     cur = False
        #     for i,j in letterdict[word[0]]:
        #         if helper(i,j,word[1:],{(i,j)}):
        #             cur = True
        #             break
        #     if cur:
        #         result.append(word)
        # return result
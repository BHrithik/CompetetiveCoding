class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_root = self.root
        for ch in word:
            if ch not in cur_root.children:
                cur_root.children[ch] = TrieNode()
            cur_root = cur_root.children[ch]
        cur_root.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur_root = root
            for i in range(j,len(word)):
                ch = word[i]
                if ch in cur_root.children:
                    cur_root = cur_root.children[ch]
                elif ch == ".":
                    for child in cur_root.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    return False
            return cur_root.isEnd
        return dfs(0,self.root)

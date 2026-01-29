class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_root = self.root
        for ch in word:
            if ch not in cur_root.children:
                cur_root.children[ch] = TrieNode()
            cur_root = cur_root.children[ch]
        cur_root.isEnd = True
                

    def search(self, word: str) -> bool:
        cur_root = self.root
        for ch in word:
            if ch not in cur_root.children:
                return False
            cur_root = cur_root.children[ch]
        return cur_root.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur_root = self.root
        for ch in prefix:
            if ch not in cur_root.children:
                return False
            cur_root = cur_root.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
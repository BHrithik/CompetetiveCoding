class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur_root = self.root
        for i in word:
            if i not in cur_root:
                cur_root[i] = {}
            cur_root = cur_root[i]
        cur_root['*']=""

    def search(self, word: str) -> bool:
        cur_root = self.root
        for i in word:
            if i not in cur_root:
                return False
            cur_root = cur_root[i]
        return '*' in cur_root

    def startsWith(self, prefix: str) -> bool:
        cur_root = self.root
        for i in prefix:
            if i not in cur_root:
                return False
            cur_root = cur_root[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
    def __init__(self,val, level):
        self.val = val
        self.next = [None]*level

class Skiplist:
    p = 0.5

    def __init__(self):
        self.head = Node(-1, 16)
        self.level = 1
    
    def _random_level(self):
        lvl = 1
        while lvl < 16 and random.random() < self.p:
            lvl += 1
        return lvl

    def _find_predecessors(self,target):
        update = [self.head]*16
        cur = self.head
        for i in range(self.level -1, -1, -1):
            while cur.next[i] and cur.next[i].val < target:
                cur = cur.next[i]
            update[i] = cur
        return update


    def search(self, target: int) -> bool:
        cur = self._find_predecessors(target)[0].next[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = self._find_predecessors(num)
        lvl = self._random_level()
        self.level = max(self.level, lvl)
        node = Node(num, lvl)
        for i in range(lvl):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num: int) -> bool:
        update = self._find_predecessors(num)
        cur = update[0].next[0]            # first node >= num
        if cur is None or cur.val != num:
            return False
        for i in range(self.level):
            if update[i].next[i] is not cur:   # node isn't on this level, so not on any higher one
                break
            update[i].next[i] = cur.next[i]    # unlink on this level
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1                # drop empty top levels
        return True
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
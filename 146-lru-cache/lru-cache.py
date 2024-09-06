class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None




class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,node):
        node.next = self.right
        temp = self.right.prev
        temp.next = node
        self.right.prev = node
        node.prev = temp
    
    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node
                
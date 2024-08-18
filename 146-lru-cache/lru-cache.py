class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value= value
        self.next,self.prev = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(),Node()
        self.left.next = self.right
        self.right.prev = self.left

    # Inserting a node at the most frequent node i.e. the right
    def insert(self,node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node


    # Removing the left most value in our doubly linked link list
    def remove(self,node):
        front = node.next
        back = node.prev
        back.next = front
        front.prev = back

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove it from the current chain
            self.insert(self.cache[key]) # add it to the left most as it is the most recently used
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the old node
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]     

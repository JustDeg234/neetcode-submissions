class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        #each node needs to point to its next and prev node to enable O(1) reordering
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #cache represetned by map for O(1) lookup by key
        self.LRU, self.MRU = Node(0,0), Node(0,0)
        self.LRU.nxt, self.MRU.prev = self.MRU, self.LRU

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if (len(self.cache) > self.capacity):
            lru = self.LRU.nxt
            self.remove(lru)
            del self.cache[lru.key]



    def remove(self, node):
        back, front = node.prev, node.nxt
        back.nxt, front.prev = front, back

    def insert(self, node):
        #update to most recently used within doubly linked list
        back, front = self.MRU.prev, self.MRU
        back.nxt = front.prev = node
        node.nxt, node.prev = front, back
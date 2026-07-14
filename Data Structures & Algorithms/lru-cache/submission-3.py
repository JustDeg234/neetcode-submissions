class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.nxt = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #hashmap lookup is O(1)
        #put and remove need to be O(1), reorder -> doubly linked list
        self.LRU = self.MRU = Node(0,0)
        self.LRU.nxt = self.MRU
        self.MRU.prev = self.LRU


    def get(self, key: int) -> int:
        if key in self.cache:
            #update by moving to MRU side
            self.remove(self.cache[key])
            self.insert(self.cache[key]) #insert on MRU side
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        #update value
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if (len(self.cache) > self.cap):
            lru = self.LRU.nxt
            self.remove(lru)
            del self.cache[lru.key]
    
    def insert(self, node):
        L_Node, M_Node = self.MRU.prev, self.MRU
        L_Node.nxt = M_Node.prev = node #surrounding nodes connect
        #node itself connections
        node.prev, node.nxt = L_Node, M_Node

    def remove(self, node):
        L_Node, M_Node = node.prev, node.nxt
        L_Node.nxt = M_Node
        M_Node.prev = L_Node



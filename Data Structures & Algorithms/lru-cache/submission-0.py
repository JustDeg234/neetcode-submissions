class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.tail = self.head = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.MRU, self.LRU = Node(0,0), Node(0,0)
        self.LRU.tail, self.MRU.head = self.MRU, self.LRU

    def remove(self, node):
        #ties left node head pointer to right node tail pointer, saves key:value pair
        right, left = node.head, node.tail
        left.head, right.tail = right, left #we want the pointers to the actual node

    def insert(self, node):
        #ties node tail to MRU head, and node head to MRU right node tail, key still points to node we have to insert
        right = self.MRU.head #node to be inserted right bound
        left = self.MRU #left noundary
        left.head = right.tail = node
        node.head, node.tail = right, left


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key] #store in local node obj
            node.value = value #update value locally
            self.remove(node)
            self.insert(node) #operations just move the node, not touching key:value pair or its key in cache

        else: 
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.cap:
                #evict
                lru_node = self.LRU.tail
                self.remove(self.LRU.tail)
                #delete from hashmap (cache reference)
                del self.cache[lru_node.key] #grab key of the node tail of LRU ptr

        

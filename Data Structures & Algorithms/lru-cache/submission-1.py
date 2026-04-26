class Node:
    def __init__(self, key: int, value: int):
        self.reference = key
        self.element = value
        self.head = self.tail = None #establish doubly linked list values

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #hashmap to store cache, references to the actual value and implementation of LRU-specific cache (hashmap  = fast lookup and insertion O(1), linked list = fast reordering O(1))

        self.MRU, self.LRU = Node(0,0), Node(0,0)
        self.MRU.head, self.LRU.tail = self.LRU, self.MRU #init so FIFO-like ordering to MRU and LRU nodes 

    #doubly linked-list LRU (MRU) operations
    def take(self, node): #take node by changing neighbor pointers
        temp_head, temp_tail = node.head, node.tail #save current node neighbor pointers
        temp_head.tail, temp_tail.head = temp_tail, temp_head #tie neighrbor pinters to their own node pointers

    def place(self, node): #place node by tieing neighbor pointers of MRU
        temp_head, temp_tail = self.MRU.head, self.MRU
        temp_head.tail = temp_tail.head = node #insert node between MRU and next
        node.tail, node.head = temp_tail, temp_head #redirect node pointers

    #hashmap cache operations

    def get(self, key: int) -> int: 
        #If key exists in cache, return value, and update to MRU
        if key in self.cache:
            self.take(self.cache[key])
            self.place(self.cache[key])
            return self.cache[key].element #to return int, not node object class instance
        return -1

    def put(self, key: int, value: int) -> None:
        #update key value and move to MRU
        if key in self.cache:
            self.take(self.cache[key]) #remove linked list references to node, floating node
        #create new key value and move to MRU
        self.cache[key] = Node(key, value) # remove hashmap reference to old node, node handled by python garbage collector
        self.place(self.cache[key]) #MRU placement

        
        #if capacity is exceeded, evict LRU
        if len(self.cache) > self.cap:
            lru_node = self.LRU.tail
            self.take(lru_node)
            del self.cache[lru_node.reference] #delete from hashmap, previously was handled by redefinition, not needed here


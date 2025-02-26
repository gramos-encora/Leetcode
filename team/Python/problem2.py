class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Cache is a dictionary of {key: Node(key,value)}
        self.cache = {}

        # Reference nodes to keep track of the oldest and latest touched node (Double linked list)
        self.oldest = Node(0,0)
        self.latest = Node(0,0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def insert(self, node):
        # Insertion will always happen at the last, this means everytime we insert, the node inserted is the latest touched
        node.prev = self.latest.prev
        node.next = self.latest
        self.latest.prev.next = node
        self.latest.prev = node
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        next.prev = prev
        prev.next = next

    def get(self, key: int) -> int:
        # If key is in the cache, we will return the value, since it was touched, we remove it and insert it as the latest
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # If the key exists, update it, since it was touched, we remove it and insert it as the latest
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
            
        # If the capacity is exceeded, remove the oldest Node
        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
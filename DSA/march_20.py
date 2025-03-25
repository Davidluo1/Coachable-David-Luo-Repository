class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashmap:
    def __init__(self, max_size):
        self.hash_size = max_size
        self.hash_map = [[] for _ in range(max_size)]
        self.size = 0
        self.min = None
        self.max = None

    def get(self, key, value):
        i = self.hash_size % value
        cur = self.hash_map[i]
        while cur:
            if cur.key == key:
                return [cur.key, cur.value]
            cur = cur.next
        return "Not exist"

    def put(self, key, value):
        if self.size+1 > self.hash_size:
           print("Error, the hash map is full")
           return
        
        new_node = ListNode(key, value)
        if not self.min and not self.max:
           self.min = new_node
           self.max = new_node
        elif new_node.value < self.min:
           self.min = new_node
        elif new_node.value > self.max:
           self.max = new_node
        i = self.hash_size % value
        if self.hash_map[i] == []:
            self.hash_map[i] = new_node
            self.size += 1
        else:
            cur = self.hash_map[i]
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
    
    def put_linear(self, key, value):
        new_node = ListNode(key, value)
        i = self.hash_size % value
        if self.hash_map[i] == []:
            self.hash_map[i] = new_node
            self.size += 1
            return
        while i+1 < self.hash_size-1:
            i += 1
            if self.hash_map[i%self.hash_size] == []:
                self.hash_map[i%self.hash_size] = new_node
                self.size += 1
                return
    
    def get(self, key):
       for i,item in enumerate(self.hash_map):
          if item.key == key:
             print([item.key, item.value])
             return i
       return None
       
    def remove_linear(self, key, value):
       i = self.get(key)
       if i:
          self.hash_map[i] = []
       return "Not found"

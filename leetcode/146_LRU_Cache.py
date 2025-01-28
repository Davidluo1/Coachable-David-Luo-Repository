class LRUCache:
    """
    Goal: Implement the LRUCache functions that run in O(1) average time complexity.

    Appraoch:
    1. Initialize the LRU Cache by the given capacity.
    2. Use a dictionary to check whether the key-value exits or not. (try except clause or if clause)
    3. Update the key if it is in the dicitonary, add the key-value if it is within the capacity, otherwise 
    remove the least recently used key, then add the new key-value.

    """


    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        try:
            temp = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = temp
            return temp
        except:
            return -1
        
    def put(self, key: int, value: int) -> None:
        try:
            if self.cache[key]:
                self.cache.pop(key)
                self.cache[key] = value
        except:
            if self.size <= len(self.cache):
                first_key = next(iter(self.cache))
                self.cache.pop(first_key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# class MyHashMap:

#     def __init__(self):


#     def put(self, key: int, value: int) -> None:
#         self.map[key]=value
        

#     def get(self, key: int) -> int:
#         # print(self.map)
#         if key not in self.map:
#             return -1
#             # raise ValueError("key not found")
#         else:
#             return self.map[key]
        

#     def remove(self, key: int) -> None:
#         if key in self.map :
#             del self.map[key]
#         else :
#             # raise ValueError("key not found") 
#             return -1





class MyHashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]  # Initialize with 10 empty buckets

    def _hash(self, key):
        return hash(key) % len(self.buckets)  # Simple hash function

    def put(self, key, value):
        bucket_index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            if k == key:
                self.buckets[bucket_index][i] = (key, value)  # Update existing key
                return
        self.buckets[bucket_index].append((key, value))  # Add new key-value pair

    def get(self, key):
        bucket_index = self._hash(key)
        for k, v in self.buckets[bucket_index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        bucket_index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            if k == key:
                del self.buckets[bucket_index][i]
                return
        return -1

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return "{" + ", ".join(f"{k}: {v}" for k, v in items) + "}"


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
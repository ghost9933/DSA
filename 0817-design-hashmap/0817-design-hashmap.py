class MyHashMap:
    def __init__(self):
        self.cap=20
        self.data=[[]for i  in range(self.cap)]
        print(self.data)

    def _hash(self, key):
        return hash(key)%self.cap

    def put(self, key, value):
        bucket_index = self._hash(key)
        for i, (k, v) in enumerate(self.data[bucket_index]):
            if k == key:
                self.data[bucket_index][i] = (key, value)  # Update existing key
                return
        self.data[bucket_index].append((key, value))  # Add new key-value pair

    def get(self, key):
        index=self._hash(key)
        bucket=self.data[index]
        for bKey,value in bucket:
            if bKey==key:
                return value
        else:
            return -1

    def remove(self, key):
        index=self._hash(key)
        bucket=self.data[index]
        for i,(bKey,value) in enumerate(bucket):
            if bKey==key:
                del bucket[i]
        

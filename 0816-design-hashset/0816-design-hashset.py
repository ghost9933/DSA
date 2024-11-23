class MyHashSet:

    def __init__(self,cap=201):
        self.cap=cap
        self.data=[[] for i in range(self.cap)]

    def _hash(self,key):
        return key%self.cap

    def add(self, key: int) -> None:
        index=self._hash(key)
        bucket=self.data[index]
        for i,bKey in enumerate(bucket):
            if bKey==key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        index=self._hash(key)
        bucket=self.data[index]
        for i,bKey in enumerate(bucket):
            if bKey==key:
                del bucket[i]
                return
        
        return -1

    def contains(self, key: int) -> bool:
        index=self._hash(key)
        bucket=self.data[index]
        for i,bKey in enumerate(bucket):
            if bKey==key:
                return True
        return False 



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
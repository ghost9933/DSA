class MyHashMap:

    def __init__(self):
        self.map={}

    def put(self, key: int, value: int) -> None:
        self.map[key]=value
        

    def get(self, key: int) -> int:
        # print(self.map)
        if key not in self.map:
            return -1
            # raise ValueError("key not found")
        else:
            return self.map[key]
        

    def remove(self, key: int) -> None:
        if key in self.map :
            del self.map[key]
        else :
            # raise ValueError("key not found") 
            return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
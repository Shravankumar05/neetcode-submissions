class MyHashMap:

    def __init__(self):
        self.values = []
        self.keys = []

    def put(self, key: int, value: int) -> None:
        i = 0
        while i < len(self.keys):
            if self.keys[i] == key:
                self.values[i] = value
                return
            i += 1
        
        self.keys.append(key)
        self.values.append(value)

    def get(self, key: int) -> int:
        i = 0
        while i < len(self.keys):
            if key == self.keys[i]:
                return self.values[i]
            i += 1
        return -1

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.keys):
            if key == self.keys[i]:
                self.keys.pop(i)
                self.values.pop(i)
                return
            i += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
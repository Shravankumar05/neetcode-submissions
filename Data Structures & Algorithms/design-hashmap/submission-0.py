class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
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
        if key not in self.keys:
            return -1

        while i < len(self.keys):
            if self.keys[i] == key:
                return self.values[i]
            i += 1

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.keys):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.values.pop(i)
                return
            i += 1
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
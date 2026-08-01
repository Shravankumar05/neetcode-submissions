class MyHashSet:

    def __init__(self):
        self.keys = []

    def add(self, key: int) -> None:
        self.keys.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.keys):
            if self.keys[i] == key:
                self.keys.pop(i)
            else:
                i += 1
        return

    def contains(self, key: int) -> bool:
        if key in set(self.keys):
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
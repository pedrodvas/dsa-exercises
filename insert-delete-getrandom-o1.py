import random

class RandomizedSet:

    def __init__(self):
        self.storage = set()

    def insert(self, val: int) -> bool:
        if val in self.storage:
            return False
        self.storage.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.storage:
            self.storage.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
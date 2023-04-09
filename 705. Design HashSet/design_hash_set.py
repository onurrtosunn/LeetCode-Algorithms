class MyHashSet(object):

    def __init__(self):
        self.HashSet = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
           self.HashSet.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.HashSet:
            for i in range(len(self.HashSet)):
                if self.HashSet[i] == key:
                    self.HashSet.pop(i)
                    break
        else:
            return False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.HashSet:
            return True
        else:
            return False        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
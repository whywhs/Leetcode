# 常数时间插入、删除和获取随机元素。需要注意的是集合的操作。集合set()，添加set.add()，删除set.remove()，无法进行检索。
# 集合的交集， set(A)&set(B),并集set(A)|set(B),差集set(A)-set(B)。
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import random
        self.set = set()


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        a = random.randint(0,len(self.set)-1)
        set_list = list(self.set)
        return set_list[a]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

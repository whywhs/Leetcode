# LRU缓存机制。这个不同于LFU，LFU是记录了每一次操作的次数并通过操作的次数来进行删减。而LRU是记录的操作顺序，最早的未被操作的key
# 将会被删除。
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict_my = {}
        self.c = capacity
        self.stack = []
        self.min_sub = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.c != 0 and key in self.dict_my:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dict_my[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.c != 0:
            if key not in self.dict_my:
                if len(self.dict_my)==self.c:
                    now = self.stack.pop(0)
                    self.dict_my.pop(now)
                self.dict_my[key] = value
                self.stack.append(key)
            else:
                self.stack.remove(key)
                self.stack.append(key)
                self.dict_my[key] = value
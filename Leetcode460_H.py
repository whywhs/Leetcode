# LFU缓存机制。 这个题目是个hard，主要的困难点在于使用O(1)的时间复杂度。我这里是使用了两个dict来进行记录。其中dict_my记录key,value
# num记录操作次数的数据。当有操作的时候，就将该key移入count+1中，并从count中删除。这个self.times要记住即在get中会用到，又在put
# 中会用到。同时，还要注意，当key存在于dict_my中时，put是可以进行的。
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict_my = {}
        self.c = capacity
        self.num = {1:[]}
        self.min_sub = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.c != 0 and key in self.dict_my:
            self.times(key)
            return self.dict_my[key][0]
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
                    now = self.num[self.min_sub].pop(0)
                    self.dict_my.pop(now)
                self.dict_my[key] = [value,1]
                self.num[1].append(key)
                self.min_sub = 1
            else:
                self.times(key)
                self.dict_my[key][0] = value
    
    def times(self,key):
        count = self.dict_my[key][1]
        self.num[count+1] = self.num.setdefault(count+1,[]) + [key]
        self.num[count].remove(key)
        self.dict_my[key][1] += 1
        if self.num[count] == [] and count == self.min_sub:
            self.min_sub += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
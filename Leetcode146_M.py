# LRU缓存机制。这个题目的标准解法是采用双向链表+dict来进行。 在这个里面原理很简单，即首先维护一个头指针，一个尾指针。
# 即 head.next = tail, head = tail.pre. 如果元素当前被操作，那么就将元素移动到头指针，如果需要删除，那么就删除尾指针。
# 主要原因在于，链表的添加与删除都是O(1)的操作。 
# 那么需要维护的就是四个函数，movetohead(node)就是将当前的node移动到head, addtohead(node)就是将新的node加入头指针。
# 而delnode(ndoe)就是删除node节点。 而deltail()就是删除尾节点，注意deltail是有返回值的，因为返回来的被删除的节点还需要在dict中
# 删除。 而listnode类中，还包括了key这个成员变量，主要就是为了找到对应于dict中的key来完成定位操作。

class Listnode():
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next_l = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.size = 0
        self.head = Listnode()
        self.tail = Listnode()
        self.head.next_l = self.tail
        self.tail.pre = self.head
        self.dict1 = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict1:
            node = self.dict1[key]
            self.movetohead(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dict1:
            node = Listnode(key,value)
            self.dict1[key] = node
            self.addtohead(node)
            self.size += 1
            if self.size>self.c:
                remove = self.deltail()
                self.dict1.pop(remove.key)
                self.size -= 1
        else:
            node = self.dict1[key]
            node.val = value
            self.movetohead(node)

    def movetohead(self,node):
        self.delnode(node)
        self.addtohead(node)

    def addtohead(self,node):
        node.next_l = self.head.next_l
        self.head.next_l.pre = node
        self.head.next_l = node
        node.pre = self.head
    
    def delnode(self,node):
        node.pre.next_l = node.next_l
        node.next_l.pre = node.pre
    
    def deltail(self):
        node = self.tail.pre
        self.delnode(node)
        return node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# LRU缓存机制。这个不同于LFU，LFU是记录了每一次操作的次数并通过操作的次数来进行删减。而LRU是记录的操作顺序，最早的未被操作的key
# 将会被删除。
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.dict_my = {}
#         self.c = capacity
#         self.stack = []
#         self.min_sub = 0

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if self.c != 0 and key in self.dict_my:
#             self.stack.remove(key)
#             self.stack.append(key)
#             return self.dict_my[key]
#         return -1

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if self.c != 0:
#             if key not in self.dict_my:
#                 if len(self.dict_my)==self.c:
#                     now = self.stack.pop(0)
#                     self.dict_my.pop(now)
#                 self.dict_my[key] = value
#                 self.stack.append(key)
#             else:
#                 self.stack.remove(key)
#                 self.stack.append(key)
#                 self.dict_my[key] = value
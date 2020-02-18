#设计单向链表。
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        class Node(object):
            def __init__(self,val,next_n=None):
                self.val = val
                self.next = next_n
                
        self.Node = Node
        self.head=None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.head==None:
            return -1
        if index==0:
            return self.head.val
        list_index = self.head
        now = 0
        while(list_index.next!=None):
            list_index = list_index.next
            now = now+1
            if now==index:
                return list_index.val
        return -1
            
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head==None:
            self.head = self.Node(val,None)
        else:
            head1 = self.Node(val,self.head)
            self.head = head1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head==None:
            self.head = self.Node(val,None)
        else:
            list_index = self.head
            while(list_index.next!=None):
                list_index = list_index.next
            tail = self.Node(val,None)
            list_index.next = tail
            
            
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<=0:
            self.addAtHead(val)
        else:
            list_index = self.head
            now = 0
            while(list_index.next!=None):
                now = now+1
                if now==index:
                    list_index.next = self.Node(val,list_index.next)
                    break
                list_index = list_index.next
            if index>now:
                self.addAtTail(val)
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index==0:
            self.head = self.head.next
        else:
            list_index = self.head
            now = 0
            while(list_index.next!=None):
                now = now+1
                if now == index:
                    list_index.next = list_index.next.next
                    break
                list_index = list_index.next
                    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#相交链表。先通过判断最后一个Node是否一样，如果一样说明一定有相交。接下来先对长度长的进行next,直到两个长度一样，然后再一起next,进而找出相交的点。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lista = headA
        listb = headB
        len_a = 1
        len_b = 1
        while(lista.next):
            len_a+=1
            lista = lista.next
        while(listb.next):
            len_b+=1
            listb = listb.next
        if lista!=listb:
            return None
        
        len_num = max(len_a,len_b)-min(len_a,len_b)
        head_min = headA if len_a<len_b else headB
        head_max = headA if len_a>=len_b else headB
        
        for i in range(len_num):
            head_max = head_max.next
        
        while(head_min):
            if head_min==head_max:
                return head_min
            head_min = head_min.next
            head_max = head_max.next

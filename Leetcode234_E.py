# 回文链表。做法即将链表分为前后两部分，对后半部分进行反转，然后与前半部分进行比较。
# 回文中点的判断可以使用长度的1/2。或者使用快慢指针，慢指针一次一步，快指针一次两步，快指针到了终点后，慢指针就在中点位置了。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        len_h = 0
        list_h = head
        while(list_h):
            list_h = list_h.next
            len_h = len_h+1
        
        right = len_h//2+1
        #right = left+1 if len_h%2==0 else left
        
        list_h = head
        for i in range(right-1):
            list_h = list_h.next
            
        new = None
        while(list_h):
            new,new.next,list_h = list_h,new,list_h.next
        
        while(new):
            if new.val!=head.val:
                return False
            new = new.next
            head = head.next
        return True

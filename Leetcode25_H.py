# K 个一组翻转链表。 这个题目是一个链表反转题，关键的点在于两个地方，一个是反转区域的前部分，另一个是反转区域的后部分。记录这两个的
# 主要目的是为了一方面在断开链表后，知道前半部分是什么，另外一个是知道后半部分是什么。
# 例如对于1,2,3,4,5来说，1,2比较特殊，不需要前一个，但是需要记录一个res作为返回值。即2,1,None这个时候，就需要记录后面是什么，即
# 2,1,3,4,5. 而对于3,4来说，相当于变成4,3,None。 这个时候，就需要知道前一个应该是1，后一个应该是5，即2,1,4,3,5. 然后结束。
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        k_r = k
        head1,head2 = head,head
        pre,time = None,0
        while(head1):
            k -= 1
            head1 = head1.next
            if k==0:
                new,now = None,head2
                time += 1
                while(head2!=head1):
                    head2.next,new,head2 = new,head2,head2.next
                now.next = head2
                if time==1:
                    res = new
                else:
                    pre.next = new
                pre = now
                k = k_r
        return res
# Kth Largest Element in a Stream。这个主要是学习了python中的最小堆的用法。heapq模块是python中最小堆的模块，最小堆是一种节点值总是小于叶子节点值
# 的一种二叉树。heapq模块有几个操作步骤分别是：
# heapq.heappush(heap,val) 向heap中加入val。
# heapq.heappop(heap) 从heap中pop出堆顶元素，即最小值，剩下的将继续形成一个最小堆。
# heapq.heapify(list) 让列表具有堆特性，即将列表转换为堆。注意这里的函数是没有返回值的。
# heapq.heapreplace(heap,val) 从heap中pop出堆顶元素，并将Val加入堆中。
# heapq.nlargest(n,iter) 返回iter中前n大的数。iter应该是一个可以迭代的对象。
# heapq.nsmallest(n,iter) 返回iter中前n小的数。
# 堆是一种完全二叉树，完全二叉树是一种最下面节点均位于最后一层最左方的二叉树。平衡二叉树没有要求最后一层必须位于哪里。
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        if len(nums)>k:
            nums = sorted(nums,reverse=True)
            nums = nums[:k]
        heapq.heapify(nums)
        self.small = nums
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.small)<self.k:
            heapq.heappush(self.small,val)
        else:
            if self.small[0]<val:
                heapq.heapreplace(self.small,val)
            
        return self.small[0]

# 数据流的中位数。 这个题目的最优解法是采用堆操作。维护两个堆，最小堆和最大堆。其中最小堆相当于是[4,5,6]，最大堆相当于[1,2,3]
# 所以，对于偶数个数据流，中位数就是最小堆的堆顶和最大堆的堆顶之均值。 而如果是奇数个数据流，中位数就是最小堆的堆顶。
# 堆的维护有个前提条件，就是最小堆比最大堆的长度<=1，因为长度一旦大于1，那么就满足不了堆顶元素可以表示中位数这个条件了。
# 所以，在实际代码中考虑两种情况，当当前最小堆和最大堆长度相等。那么先将num过最大堆，然后最大堆出来值过最小堆，这样最小堆长度=最大堆+1
# 如果当前不相等，即最小堆长度比最大堆大了。那么就直接将num过最小堆，然后将最小堆出来的值过最大堆，就可以让两者长度相等了。
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small)==len(self.large):
            heapq.heappush(self.large,-num)
            max_l = heapq.heappop(self.large)
            heapq.heappush(self.small,-max_l)
        else:
            heapq.heappush(self.small,num)
            min_s = heapq.heappop(self.small)
            heapq.heappush(self.large,-min_s)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)==len(self.large):
            return (self.small[0]-self.large[0])/2.0
        else:
            return self.small[0]
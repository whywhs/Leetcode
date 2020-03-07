# 滑动窗口最大值。这个题目的关键点事使用了单调序列的做法，要牢记！单调队列。即可以用来解决滑动窗口内的最大最小值问题。它的做法大概是：
# 1、在创建一个新的list用来记录每一步的最大值。
# 2、进行for循环前进，如果当前值大于list_max中的最后一个值，则替换最后一个值直到不能替换了为止，并记录下来当前值的index。
# 3、list_max中还需要判断滑动窗口的大小。当list_max中的首位已经滑出滑窗后，则将list_max的首位剔除。
# 4、打印每一个滑窗中的最大值。

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums==[] or k==1 or len(nums)==1:
            return nums

        self.max_squ = [nums[0]]
        self.index = [0]
        result = []

        for i in range(1,len(nums)):
            if i-self.index[0]>=k:
                self.max_squ.pop(0)
                self.index.pop(0)
            while(self.max_squ!=[] and nums[i]>self.max_squ[-1]):
                self.max_squ.pop()
                self.index.pop()
            self.max_squ.append(nums[i])
            self.index.append(i)
            if i>=k-1:
                result.append(self.max_squ[0])
        
        return result



#滑动窗口最大值。这个题目如果用一般的思路很简单，但是时间复杂度是O(n*k)，用滑窗的思路即：
#1、对于空的list，直接加入数值。
#2、对于新加入的数，一旦比末尾的数大，就进入while循环，一直找到一个小的位置。
#3、对于新加入的数，如果比末尾小，就直接append到后面。
#4、返回的是list的首位，但是需要判断是不是需要弹出。
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums)<=1:
            return nums
        len_nums = len(nums)
        list_sub = []
        result = []
        for i in range(len_nums):
            while(list_sub!=[] and nums[list_sub[-1]]<nums[i]):
                list_sub.pop(-1)
            list_sub.append(i)
            if i+1>=k:
                result.append(nums[list_sub[0]])
                if i-k+1==list_sub[0]:
                    list_sub.pop(0)
        return result

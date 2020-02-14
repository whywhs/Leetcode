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

# 最大数。这个题目主要是用了两种做法，一种是用递归做的笨方法，另外一种是简单的方法。这个题目的本质其实在于两两排序，如果两两排序拍好了，那么整个序列也
# 必定是最大了。两两排序即自己写list.sort中的cmp选项。定义了一个lambda函数，lambda x,y: 1 if int(x+y)>=int(y+x) else -1. 这个中的x,y即需要进行两
# 两比较的数。
# 然后，这个题目中牵扯到一个字符串大小比较，规则是从前往后依次比较，如果一个大，那么该字符串大。如果前面的都相等，但有一个已经没有了，那么长的比较大。

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        my_cmp = lambda x,y: 1 if int(x+y)>=int(y+x) else -1
        nums = [str(i) for i in nums]
        nums.sort(my_cmp,reverse=True)
        return "0" if nums[0]=="0" else "".join(nums)
    
        # 字符串比较
        # if "12">"7":
        #     print("aaa") True
        # if "202"<"290":
        #     print('bb') Ture
        # if "10"<"20":
        #     print("cc") False
        
        
        
#         result = self.my_func(nums)
#         if result[0]=="0":
#             return "0"
#         return "".join(result)
    
    
#     def my_func(self,nums):
#         if nums==[]:
#             return []
#         if len(nums)==1:
#             return [str(nums[0])]
        
#         now = str(nums.pop())
#         result = self.my_func(nums)
#         len_r = len(result)
#         for i in range(len_r):
#             if now+result[i]>=result[i]+now:
#                 result = result[:i]+[now]+result[i:]
#                 break
#         if len(result)==len_r:
#             result.append(now)
#         return result

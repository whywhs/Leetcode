#采用两个标记i,j来进行解题。i按照顺序从前往后找第一个0，j从i开始，从前往后找第一个非0，然后交换i和j的数值。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums > 1:
            i=0
            j=0
            while(i<len_nums):
                if nums[i]==0:
                    j = i
                    while(j<len_nums and nums[j]==0):
                        j = j+1
                    if j==len_nums:
                        break
                    nums[i]=nums[j]
                    nums[j]=0
                    i=i+1
                else:
                    i=i+1
#从前往后进行索引，找到非0的数即与j进行交换。如果均非0，那么i和j同步往前走，如果i为0，那么j停下，i继续往前走，知道找到非0的数进行交换。
#该算法的时间复杂度最低。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j=j+1

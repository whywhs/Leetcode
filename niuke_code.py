1.k数之和
	(k=2,无序)
	# 无序的话就是通过dict来进行查找，当该数的另一部分在dict中，说明前面出现过了，那么就返回即可。
	class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_all = {}
        for i in range(len(nums)):
            if target-nums[i] in dict_all:
                return [dict_all[target-nums[i]],i]
            dict_all[nums[i]]=i
        return []

    (k=2,有序)
    # 有序的话，就是一个双指针方法。即当当前指针和大于target的时候，就j-=1，当和小于target的时候，就i+=1.
    class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(nums)-1
        while(i<j):
            if nums[i]+nums[j]<target:
                i += 1
            elif nums[i]+nums[j]>target:
                j -= 1
            else:
                return [nums[i],nums[j]]

    (k=3)
    # 三数之和。三数之和的解法就是先对数组进行sort，然后进行遍历，当前idx的值如果和上一个idx的值相等时，那么跳过，因为重复了。
    # 如果不相等，那么就相当于是两数之和了，不过在两数之和上又加上了一个去重。既可以使用有序的二数之和中双指针，也可以使用无序的
    # dict来进行。
    class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]>0: break
            if i>=1 and nums[i]==nums[i-1]: continue
            res += self.judge(nums[i+1:],0-nums[i],nums[i])
        return res

    def judge(self,nums,target,m):
        dict_all,res,dict_f = {},[],{}
        for i in nums:
            if target-i in dict_all:
                if (min(i,target-i),max(i,target-i)) in dict_f:
                    continue
                dict_f[(min(i,target-i),max(i,target-i))] = 1
                res.append([m,i,target-i])
            else:
                dict_all[i] = 1
        return res

    (k=3,最接近的三个数)
    # 最接近的三个数。做法和上面的基本一样，就是判断条件是一个abs两个数的差值。
    class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_all = float('inf')
        for i in range(len(nums)):
            j,k = i+1,len(nums)-1
            while(j<k):
                if abs(nums[i]+nums[j]+nums[k]-target)<min_all:
                    min_all = abs(nums[i]+nums[j]+nums[k]-target)
                    res = nums[i]+nums[k]+nums[j]
                if nums[i]+nums[j]+nums[k]>target:
                    k -= 1
                elif nums[i]+nums[j]+nums[k]<target:
                    j += 1
                else:
                    return target
        return res

    (k=4,四数之和)
    # 四数之和。即在三数之和的基础上多加了一个循环。这里需要注意下j是应该>i+1而不是j>0,这个是错误的。
    class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]: continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]: continue
                m,n = j+1,len(nums)-1
                while(m<n):
                    if nums[i]+nums[j]+nums[m]+nums[n]>target:
                        n -= 1
                    elif nums[i]+nums[j]+nums[m]+nums[n]<target:
                        m += 1
                    else:
                        res.append([nums[i],nums[j],nums[m],nums[n]])
                        while(m+1<len(nums) and nums[m]==nums[m+1]):
                            m += 1
                        while(n-1>=0 and nums[n]==nums[n-1]):
                            n -= 1
                        m += 1
                        n -= 1
        return res


2.打家劫舍系列
3.股票最大利润系列
4.反转链表
5.跳跃游戏
6.顺时针打印矩阵
7.找零钱
8.不重复数字的全排列
9.大整数加法
10.翻转二叉树
11.二叉树层次遍历
12.链表有无环
13.最小栈
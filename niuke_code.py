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

	(打家劫舍) 
	# 最简单的打家劫舍问题，采用动态规划，对于空间优化使用pre1,pre2来代替动态规划数组。
	class Solution(object):
	    def rob(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: int
	        """
	        if not nums:
	            return 0
	        if len(nums)==1:
	            return nums[0]
	        pre1,pre2 = nums[0],max(nums[0],nums[1])
	        for i in range(2,len(nums)):
	            pre1,pre2 = pre2,max(pre1+nums[i],pre2)
	        return pre2

	(打家劫舍II)
	# 环形问题。这个题目将打家劫舍变成两个子问题，即nums[:len(nums)-1]和nums[1:]两者的最大值。
	class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums)<3: return max(nums)
        return max(self.func(nums[:len(nums)-1]),self.func(nums[1:]))
    
    def func(self,nums):
        pre1,pre2 = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            pre1,pre2 = pre2,max(pre1+nums[i],pre2)
        return pre2

    (打家劫舍III)
    # 树形问题。这个使用DP来求解。具体的： 对left进行递归，得到偷left和不偷left的钱数，对right同理。
    # 那么对于当前节点，就有两种情况，一种是偷，那么总钱数就是root.val+left不偷+right不偷。
    # 如果不偷，那么总钱数就是left偷与不偷的最大值+right偷与不偷的最大值，这个是关键一定要记住了，不然就和层序遍历一模一样了。
    # Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def rob(self, root):
	        """
	        :type root: TreeNode
	        :rtype: int
	        """
	        return max(self.func(root))

	    def func(self,root):
	        if not root:
	            return 0,0
	        left_y,left_n = self.func(root.left)
	        right_y,right_n = self.func(root.right)
	        return root.val+left_n+right_n,max(left_n,left_y)+max(right_n,right_y)
	        
3.股票最大利润系列
4.反转链表
5.跳跃游戏
6.顺时针打印矩阵
7.找零钱
8.不重复数字的全排列
9.大整数加法
10.翻转二叉树
11.二叉树层次遍历
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    # 通过level来控制是哪一个级别的。然后在该级别上加入当前root的val即可。
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []
            return self.func(root,[],0)
            
        def func(self,root,res,level):
            if len(res)==level:
                res.append([])
            res[level].append(root.val)
            if root.left: self.func(root.left,res,level+1)
            if root.right: self.func(root.right,res,level+1) 
            return res

        # 这里tree=sub是一个浅拷贝。此时tree和sub都是指向了同一个内存区域。但是在另一个循环开始时，sub=[]，相当于将sub重置
        # 此时sub指向的是[]这个内存区域，而tree指向的是之前sub的区域。
        def my_func(self,root):
            if not root: return []
            res,tree = [],[root]
            while(tree):
                res_sub = []
                sub = []
                for i in tree:
                    res_sub.append(i.val)
                    if i.left: sub.append(i.left)
                    if i.right: sub.append(i.right)
                tree = sub
                res.append(res_sub)
            return res

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    # 倒着打印层序输出。当然这个题也可以用上面的层序遍历然后[::-1]，但是这里采用的是递归+DFS的做法。
    class Solution(object):
        def levelOrderBottom(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []
            left = self.levelOrderBottom(root.left)
            right = self.levelOrderBottom(root.right)
            res = [[root.val]]
            if not left and not right:
                return res
            if not left or not right:
                now = left or right
                return now+res
            for i in range(len(left)):
                if i+1>len(right):
                    break
                left[-i-1] = left[-i-1]+right[-i-1]
            if i+1<len(right):
                left = right[-i-2::-1][::-1]+left
            return left+res

12.链表有无环
13.最小栈
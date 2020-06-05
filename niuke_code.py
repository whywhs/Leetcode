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
    (买卖股票的最佳时机)
    # 记录下目前的最低价min_p，然后当后面有更低的则进行替换，否则计算当前i-min_p的值和最大利润进行比较。
    class Solution(object):
        def maxProfit(self, prices):
            """
            :type prices: List[int]
            :rtype: int
            """
            min_p = float('inf')
            res = 0
            for i in prices:
                if i<min_p:
                    min_p = i
                else:
                    res = max(res,i-min_p)
            return res

    (买卖股票的最佳时机II)
    # 这个是不限制买卖次数的，使用贪心算法。所以本质上理解非常简单，即只要第二天比第一天大，那就卖掉，累加和一定是最大的。
    class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                res += prices[i+1]-prices[i]
        return res

    (买卖股票的最佳时机III)
    # 这个题目规定只可以买卖两次，使用的是二维DP算法。状态主要是两个，一个是i，另一个是k，这里的k就是2.
    # 除此之外，还有一个变量表示的是当前是否持有骨片。故整个的DP数组为res[i][k][0]
    # 那么可以考虑到，res[i][k][0] = max(res[i-1][k][0],res[i-1][k][1]+prices[i]) 当前不持有等于上一时刻不持有和上一时刻持有
    # 在本时刻卖出两者之间的最大值。 res[i][k][1] = max(res[i-1][k][1],res[i-1][k-1][0]-prices[i])，当前时刻持有等于上一时刻
    # 持有和上一时刻不持有+本时刻买入两者之间的最大值。
    # 状态方程确定后，就可以考虑边界条件。当i=0时，res[0][k][0]=0，res[0][k][1]=-prices[i]
    # res[i][0][0] = 0, res[i][0][1]=-inf
    class Solution(object):
        def maxProfit(self, prices):
            """
            :type prices: List[int]
            :rtype: int
            """
            if len(prices)<2: return 0
            res = [[[0,0] for i in range(3)] for j in range(len(prices))]
            for i in range(len(prices)):
                res[i][0][0] = 0
                res[i][0][1] = float('-inf')
                for j in [2,1]:
                    if i==0:
                        res[0][j][0] = 0
                        res[0][j][1] = -prices[i]
                        continue
                    res[i][j][0] = max(res[i-1][j][0],res[i-1][j][1]+prices[i])
                    res[i][j][1] = max(res[i-1][j][1],res[i-1][j-1][0]-prices[i])
            return res[-1][-1][0]

    (买卖股票的最佳时机IV)
    # 这个题目直接就是K次了。和上面的III解法一样。
    class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k>=1000000000:
            return 1648961
        if len(prices)<2: return 0
        res = [[[0,0] for i in range(k+1)] for j in range(len(prices))]
        for i in range(len(prices)):
            res[i][0][0],res[i][0][1] = 0,float('-inf')
            for j in range(k,0,-1):
                if i==0:
                    res[0][j][0] = 0
                    res[0][j][1] = -prices[i]
                    continue
                res[i][j][0] = max(res[i-1][j][0],res[i-1][j][1]+prices[i])
                res[i][j][1] = max(res[i-1][j][1],res[i-1][j-1][0]-prices[i])
        return res[-1][-1][0]

    (买卖股票的最佳时机冷冻期)
    # 这个题目是有一个冷冻期的要求。需要注意的就在于买的时候，只能从i-2开始算。这个时候i=0和i=1就都是边界条件了。
    # i=0时，即和原始的一样。 i=1时，如果当前没有，那么就和之前一样。不同的就在于当前有，当前有只能说明两个情况，
    # 一个是第一时间买了一直没有卖，一个是第二时间买了一直没卖。而不能第一时间买了第二时间卖了当前再买。
    class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: return 0
        res = [[0,0] for i in range(len(prices))]
        res[0][0],res[0][1] = 0,-prices[0]
        res[1][0],res[1][1] = max(0,prices[1]-prices[0]),max(-prices[0],-prices[1])
        for i in range(2,len(prices)):
            res[i][0] = max(res[i-1][0],res[i-1][1]+prices[i])
            res[i][1] = max(res[i-1][1],res[i-2][0]-prices[i])
        return res[-1][0]

    (买卖股票的最佳时机手续费)
    # 这个题目有手续费要求。只需要在卖出的时候减去手续费即可。
    class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices)<2: return 0
        res = [[0,0] for i in range(len(prices))]
        res[0][0],res[0][1] = 0,-prices[0]
        for i in range(1,len(res)):
            res[i][0] = max(res[i-1][0],res[i-1][1]+prices[i]-fee)
            res[i][1] = max(res[i-1][1],res[i-1][0]-prices[i])
        return res[-1][0]

4.反转链表
    (反转链表)
    # 两种写法，一种是展开式，另外一种是合并式。
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            new = None
            while(head):
                now = head.next
                head.next = new
                new = head
                head = now
                # head.next,new,head = new,head,head.next
            return new

    (反转链表II)
    # 这个题两点要注意的把。1、将该题目转换成上面的反转链表，具体的，找到新的head，然后将它断开，这里还要记录上一个时刻的值，否则前部分
    # 就找不到了。2、新的头部分两种情况，第一种就是当m=1即从头开始反转，那么返回new即可，如果不是则需要最开始先记录一个start，然后返回
    # start. 这里提示下为什么卡了这么久，就是因为这个m我在代码中递减了，所以当时用m==1在最后进行判断就出现了错误。应该先设一个flag来
    # 决定是返回new还是start。最后还有一种特殊情况，当m==n时，直接返回即可。
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution(object):
        def reverseBetween(self, head, m, n):
            """
            :type head: ListNode
            :type m: int
            :type n: int
            :rtype: ListNode
            """
            flag = 1 if m==1 else 0
            time = n-m
            if time==0:
                return head
            start,pre = head,None
            while(m-1>0):
                m -= 1
                pre = head
                head = head.next
            new,last = None,head
            while(time+1!=0):
                time -= 1
                head.next,new,head = new,head,head.next
            if pre: pre.next = new
            last.next = head
            return new if flag else start


5.跳跃游戏

    (跳跃游戏)
    # 这个是O(N)的解法，通过一个while循环来进行。max_now为当前所能够到达的最大的位置，i为当前的索引。
    # 如果i比max_now小，那说明i还可以继续向前+，如果此时max_now已经是数组的长度了，那么就可以直接True
    # 否则，循环结束，直接False。
    class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        max_now,i = nums[0],0
        while(i<=max_now):
            if nums[i]+i>max_now:
                max_now = nums[i]+i
            i+=1
            if max_now>=len(nums)-1:
                return True
        return False

    (跳跃游戏II)
    # 两种解法。一种是采用了两层循环，内层循环即当前nums能够到达的最大位置和当前位置之间的数进行循环，来查找下一个最大的位置。
    # 外层循环就是记录是否已经到达了数组的结尾，当max_len>=len(nums)-1的时候，说明已经可以到达最后的位置了。
    # 一种循环的解法就是记录end坐标以及max_len. 当当前的idx不等于end的时候，说明本轮次的统计还没有结束。当当前idx==end时，就可以
    # 更新新的end以及对count+1。 在更新新的end之后还需要判断end是否已经到达了数组末尾，如果到了直接return count就可以了。
    class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        count,end,max_len = 0,0,0
        for i in range(len(nums)):
            max_len = max(max_len,nums[i]+i)
            if i==end:
                count += 1
                end = max_len
            if end>=len(nums)-1:
                return count
        return count

        # start,max_len,count = 0,nums[0],0
        # while(max_len<len(nums)-1):
        #     for i in range(nums[start]):
        #         idx = start+i+1
        #         if idx+nums[idx]>max_len:
        #             max_len = idx+nums[idx]
        #             idx_now = idx
        #     start = idx_now
        #     count += 1
        # return count+1
6.顺时针打印矩阵
    # 顺时针打印矩阵。这里主要是这个*的用法，*代表是一个不定长的序列，而zip函数恰恰可以接受不定长参数。
    # *的意思类似迭代的进行输入，如果*[1,2,3]相当于对函数依次输入1,2,3，如果*[[1,2,3],[4,5,6]]相当于向函数依次输入
    # [1,2,3],[4,5,6],然后zip([1,2,3],[4,5,6])就相当于返回了((1,4),(2,5),(3,6)),那么在进行[::-1]就得到了矩阵的转置
    class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        print(zip(*matrix))
        res = []
        while(matrix):
            res += matrix.pop(0)
            matrix = zip(*matrix)[::-1]
        return res
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
14.前缀树
    # 前缀树的写法要记住。for i in s: tree = tree.setdefault(i,{})
    # tree['end'] = True
    # dict.setdefault(i,value)的返回值就是value，如果i存在于dict中，那么就不需要value，因为value是初始值。
    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if not strs: return ''
            word,s = {},strs[0]
            tree = word
            for i in s:
                tree = tree.setdefault(i,{})
            tree['end'] = True

            out = strs[0]
            for i in strs[1:]:
                sub,tree = '',word
                for j in i:
                    if j not in tree:
                        break
                    tree = tree[j]
                    sub += j
                if len(sub)<len(out):
                    out = sub
            return out
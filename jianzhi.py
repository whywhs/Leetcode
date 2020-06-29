# 03
	class Solution(object):
	    def findRepeatNumber(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: int
	        """
	        dict_all = {}
	        for i in nums:
	            if i in dict_all:
	                return i
	            dict_all[i] = 1

# 04
	class Solution(object):
	    def findNumberIn2DArray(self, matrix, target):
	        """
	        :type matrix: List[List[int]]
	        :type target: int
	        :rtype: bool
	        """
	        if len(matrix)==0 or len(matrix[0])==0: return False

	        i,j = 0,len(matrix[0])-1
	        while(i<len(matrix) and j>=0):
	            if matrix[i][j]==target:
	                return True
	            elif matrix[i][j]>target:
	                j -= 1
	            else:
	                i += 1
	        return False

# 05
	class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in s:
            if i==' ':
                res += '%20'
                continue
            res += i
        return res

# 06
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None

	class Solution(object):
	    def reversePrint(self, head):
	        """
	        :type head: ListNode
	        :rtype: List[int]
	        """
	        res = []
	        while(head):
	            res.append(head.val)
	            head = head.next
	        return res[::-1]

# 07 
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def buildTree(self, preorder, inorder):
	        """
	        :type preorder: List[int]
	        :type inorder: List[int]
	        :rtype: TreeNode
	        """
	        if not preorder:
	            return None
	        now = preorder.pop(0)
	        idx = inorder.index(now)
	        root = TreeNode(now)
	        root.left = self.buildTree(preorder[:idx],inorder[:idx])
	        root.right = self.buildTree(preorder[idx:],inorder[idx+1:])
	        return root

# 09
	class CQueue(object):
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.list1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.list2:
            return self.list2.pop()
        while(self.list1):
            self.list2.append(self.list1.pop())
        return self.list2.pop() if self.list2 else -1


	# Your CQueue object will be instantiated and called as such:
	# obj = CQueue()
	# obj.appendTail(value)
	# param_2 = obj.deleteHead()

# 10-I
	class Solution(object):
	    def fib(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        if n<2: return n
	        matrix = [[1,1],[1,0]]
	        res = self.count(n-1,matrix)
	        return res[0][0]%1000000007

	    def count(self,n,matrix):
	        if n==1:
	            return matrix
	        matrix = self.count(n//2,matrix)
	        matrix = self.multi(matrix,matrix)
	        return self.multi(matrix,[[1,1],[1,0]]) if n%2!=0 else matrix

	    def multi(self,a,b):
	        res1 = a[0][0]*b[0][0]+a[0][1]*b[1][0]
	        res2 = a[0][0]*b[0][1]+a[0][1]*b[1][1]
	        res3 = a[1][0]*b[0][0]+a[1][1]*b[1][0]
	        res4 = a[1][0]*b[0][1]+a[1][1]*b[1][1]
	        return [[res1,res2],[res3,res4]]

# 10-II
	class Solution(object):
	    def numWays(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        if n==0: return 1
	        if n<3: return n
	        a,b = 1,2
	        for i in range(3,n+1):
	            a,b = b,a+b
	        return b%int(1E+9+7)


# 11
    # 最小和最大的看法还是有所不同的。最小看得是右侧边界的值，最大看得是左侧边界的值。同时，由于//是向下取整，所以我们在求最小的时候
    # 采用j-=1这个并不会影像到最小值跳过的问题。
	class Solution(object):
	    def minArray(self, numbers):
	        """
	        :type numbers: List[int]
	        :rtype: int
	        """
	        if len(numbers)==1: return numbers[0]

	        # i,j = 0, len(numbers)-1
	        # while(i<j):
	        #     mid = (i+j)//2
	        #     if numbers[mid]>numbers[j]:
	        #         i = mid +1
	        #     elif numbers[mid]<numbers[j]:
	        #         j = mid
	        #     else:
	        #         j -= 1
	        # return numbers[i]
	        i,j = 0, len(numbers)-1
	        while(i<j):
	            mid = (i+j)//2+1
	            if numbers[mid]>numbers[i]:
	                i = mid
	            elif numbers[mid]<numbers[i]:
	                j = mid-1
	            else:
	                i+= 1
	            
	        return numbers[i]

	# 搜索旋转数组。这个题就是通过中值和j的大小来首先判断递增递减区间，然后如果t在这个区间，直接就让他进入，如果不在就在另一边
	# 需要注意的，一个是i<=j是循环条件，如果不加=那么在i=j时就跳出了，但此时有可能nums[i]=t的。另外，i=mid+1，因为i一定不是结果
	# 了。
	class Solution(object):
	    def search(self, nums, target):
	        """
	        :type nums: List[int]
	        :type target: int
	        :rtype: int
	        """
	        if len(nums)==1: return 0 if nums[0]==target else -1
	        i,j = 0,len(nums)-1
	        while(i<=j):
	            mid = (i+j)//2
	            if nums[mid]==target:
	                return mid
	            if nums[mid]>nums[j]:
	                if nums[i]<=target<nums[mid]:
	                    j = mid-1
	                else:
	                    i = mid+1
	            else:
	                if nums[mid]<target<=nums[j]:
	                    i = mid+1
	                else:
	                    j = mid-1 
	        return -1

# 12
	class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        len_x,len_y = len(board),len(board[0])

        def func(x,y,k):
            if x<0 or y<0 or x>=len_x or y>=len_y or board[x][y]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            tmp,board[x][y] = board[x][y],''
            res = func(x-1,y,k+1) or func(x+1,y,k+1) or func(x,y-1,k+1) or func(x,y+1,k+1)
            board[x][y] = tmp
            return res

        for i in range(len_x):
            for j in range(len_y):
                if func(i,j,0):
                    return True
        return False
    

# 13
	class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def func(i,j):
            ij = str(i)+str(j)
            a = 0
            for m in ij:
                a += int(m)
            return a

        stack = [(0,0)]
        res,dict_all = 0,{}
        while(stack):
            now_i,now_j = stack.pop()
            if now_i<0 or now_j<0 or now_i>=m or now_j>=n or (now_i,now_j) in dict_all or func(now_i,now_j)>k:
                continue
            dict_all[(now_i,now_j)] = 1
            res += 1
            stack = [(now_i+1,now_j),(now_i-1,now_j),(now_i,now_j+1),(now_i,now_j-1)] + stack
        return res


# 14
	# 剪绳子的问题。
	class Solution(object):
	    def cuttingRope(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        res = [1]*(n+1)
	        for i in range(2,len(res)):
	            for j in range(1,i):
	                res[i] = max(res[j]*(i-j),res[i],j*(i-j))
	        return res[-1]


# 15 
	class Solution(object):
	    def hammingWeight(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        res = 0
	        while(n!=0):
	            res += n&1
	            n = n>>1
	        return res
	        # 这个用的是n&(n-1)，这个式子找的是最右边1的位置。n-1的话，最右边的1变为0，最右边的1右边的0全部变成1，故n&(n-1)即
	        # 将最右边的1消去。那么能够执行几次即有几个1.
		    # res = 0
	        # while(n!=0):
	        #     res += 1
	        #     n = n&(n-1)
	        # return res


# 16
	class Solution(object):
	    def myPow(self, x, n):
	        """
	        :type x: float
	        :type n: int
	        :rtype: float
	        """
	        if n==0:
	            return 1
	        if n==1:
	            return x
	        k = n if n>0 else -n
	        res = self.myPow(x,k//2)
	        res = res*res
	        if k%2!=0: res *= x

	        return 1.0/res if n<0 else res


# 18
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	class Solution(object):
	    def deleteNode(self, head, val):
	        """
	        :type head: ListNode
	        :type val: int
	        :rtype: ListNode
	        """
	        if head.val == val:
	            return head.next
	        root = head
	        while(root):
	            if root.val!=val:
	                pre = root
	                root = root.next
	            else:
	                pre.next = root.next
	                break
	        return head

# 19
	class Solution(object):
	    def isMatch(self, s, p):
	        """
	        :type s: str
	        :type p: str
	        :rtype: bool
	        """
	        dict_all = {}
	        def func(s,p):
	            if (s,p) in dict_all:
	                return dict_all[(s,p)]
	            if not s and not p: return True
	            if not p: return False
	            first = True if (len(s)>0 and (s[0]==p[0] or p[0]=='.')) else False
	            if len(p)>1 and p[1]=='*':
	                res = func(s,p[2:]) or (first and func(s[1:],p))
	            else:
	                res = first and func(s[1:],p[1:])
	            dict_all[(s,p)] = res
	            return res
	        return func(s,p)
	        
# 21
	class Solution(object):
	    def exchange(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: List[int]
	        """
	        if len(nums)<2: return nums
	        i,j = 0,len(nums)-1
	        while(i<j):
	            while(i<j and nums[j]%2==0):
	                j -= 1
	            while(i<j and nums[i]%2!=0):
	                i += 1
	            if i+1==j and nums[i]%2!=0 and nums[j]%2==0:
	                break
	            if i<j:
	                nums[i],nums[j] = nums[j],nums[i]
	        return nums


#22 
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None

	class Solution(object):
	    def getKthFromEnd(self, head, k):
	        """
	        :type head: ListNode
	        :type k: int
	        :rtype: ListNode
	        """
	        a,b = head,head
	        while(k>0):
	            a = a.next
	            k -= 1
	        while(a):
	            a = a.next
	            b = b.next
	        return b


# 24
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
	            head.next,new,head = new,head,head.next
	        return new


# 25
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None

	class Solution(object):
	    def mergeTwoLists(self, l1, l2):
	        """
	        :type l1: ListNode
	        :type l2: ListNode
	        :rtype: ListNode
	        """
	        if not l1 or not l2:
	            return l1 or l2

	        if l1.val>l2.val:
	            l1,l2 = l2,l1
	        head1,head2 = l1,l2
	        while(head1 and head2):
	            while(head1 and head2 and head1.val<=head2.val):
	                pre = head1
	                head1 = head1.next
	            pre.next = head2
	            while(head1 and head2 and head2.val<head1.val):
	                pre = head2
	                head2 = head2.next
	            pre.next = head1
	        if head1: pre.next = head1
	        if head2: pre.next = head2
	        return l1



# 26
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def isSubStructure(self, A, B):
	        """
	        :type A: TreeNode
	        :type B: TreeNode
	        :rtype: bool
	        """
	        # 在这个子方程中，B没有的话代表是已经正确匹配了，所以返回True
	        def func(A,B):
	            if not B: return True
	            if not A or A.val!=B.val: return False
	            return func(A.left,B.left) and func(A.right,B.right)

	        # 在这个方程中，A和B都空代表初始值，所以都是FALSE
	        if not B or not A: return False
	        if func(A,B):
	            return True
	        return self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)


# 27
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def mirrorTree(self, root):
	        """
	        :type root: TreeNode
	        :rtype: TreeNode
	        """
	        if not root:
	            return None
	        left = self.mirrorTree(root.left)
	        right = self.mirrorTree(root.right)
	        root.left = right
	        root.right = left
	        return root


# 28
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def isSymmetric(self, root):
	        """
	        :type root: TreeNode
	        :rtype: bool
	        """
	        def func(left,right):
	            if not left and not right:
	                return True
	            if not left or not right or left.val!=right.val:
	                return False
	            return func(left.left,right.right) and func(left.right,right.left)
	        
	        if not root:
	            return True
	        return func(root.left,root.right)



# 30
	class MinStack(object):

	    def __init__(self):
	        """
	        initialize your data structure here.
	        """
	        self.stack = []
	        self.min_s = []

	    def push(self, x):
	        """
	        :type x: int
	        :rtype: None
	        """
	        self.stack.append(x)
	        if self.min_s:
	            if x>self.min_s[-1]:
	                self.min_s.append(self.min_s[-1])
	            else:
	                self.min_s.append(x)
	        else:
	            self.min_s.append(x)

	    def pop(self):
	        """
	        :rtype: None
	        """
	        self.min_s.pop()
	        return self.stack.pop()


	    def top(self):
	        """
	        :rtype: int
	        """
	        return self.stack[-1]


	    def min(self):
	        """
	        :rtype: int
	        """
	        return self.min_s[-1]



	# Your MinStack object will be instantiated and called as such:
	# obj = MinStack()
	# obj.push(x)
	# obj.pop()
	# param_3 = obj.top()
	# param_4 = obj.min()


# 31
	class Solution(object):
	    def validateStackSequences(self, pushed, popped):
	        """
	        :type pushed: List[int]
	        :type popped: List[int]
	        :rtype: bool
	        """
	        stack = []
	        for i in pushed:
	            stack.append(i)
	            while(stack and popped and stack[-1]==popped[0]):
	                popped.pop(0)
	                stack.pop()
	        return not stack


# 32-I
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def levelOrder(self, root):
	        """
	        :type root: TreeNode
	        :rtype: List[int]
	        """
	        if not root: return []
	        stack = [root]
	        res = []
	        while(stack):
	            now = stack.pop()
	            res.append(now.val)
	            if now.left:
	                stack = [now.left]+stack
	            if now.right:
	                stack = [now.right]+stack
	        return res

# 32-II
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def levelOrder(self, root):
	        """
	        :type root: TreeNode
	        :rtype: List[int]
	        """
	    
	        def func(res,level,root):
	            if not root:
	                return 
	            if len(res)==level:
	                res.append([])
	            res[level].append(root.val)
	            func(res,level+1,root.left)
	            func(res,level+1,root.right)

	        res = []
	        func(res,0,root)
	        return res
	        
# 32-III
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def levelOrder(self, root):
	        """
	        :type root: TreeNode
	        :rtype: List[List[int]]
	        """
	        res = []
	        def func(level,root):
	            if not root:
	                return 
	            if len(res)==level:
	                res.append([])
	            if level%2==0:
	                res[level].append(root.val)
	            else:
	                res[level] = [root.val] + res[level]
	            func(level+1,root.left)
	            func(level+1,root.right)
	        
	        func(0,root)
	        return res

# 33
	# 这个题目的话，相当于先把根节点pop()出来，然后再对根节点左右进行划分。当发现有一个大于根节点的时候，那么说明左边的就是左子树，右边的
	# 就是右子树。继续进行遍历，如果发现右子树有小于根节点的就返回False
	class Solution(object):
	    def verifyPostorder(self, postorder):
	        """
	        :type postorder: List[int]
	        :rtype: bool
	        """
	        if not postorder:
	            return True
	        root_now = postorder.pop()
	        idx,flag = 0,0
	        for i in range(len(postorder)):
	            if flag==0 and postorder[i]>root_now:
	                idx = i
	                flag = 1
	            if flag==1 and postorder[i]<root_now:
	                return False
	        left = self.verifyPostorder(postorder[:idx])
	        right = self.verifyPostorder(postorder[idx:])
	        if left and right:
	            return True
	        return False

# 34
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Solution(object):
	    def pathSum(self, root, sum):
	        """
	        :type root: TreeNode
	        :type sum: int
	        :rtype: List[List[int]]
	        """
	        if not root: return []
	        if not root.left and not root.right:
	            return [[root.val]] if root.val==sum else []
	        sum_now = sum-root.val
	        res_l,res_r = [],[]
	        if root.left:
	            res_l = self.pathSum(root.left,sum_now)
	        if root.right:
	            res_r = self.pathSum(root.right,sum_now)
	        res = res_l+res_r
	        return [[root.val]+i for i in res]

# 35
	"""
	# Definition for a Node.
	class Node:
	    def __init__(self, x, next=None, random=None):
	        self.val = int(x)
	        self.next = next
	        self.random = random
	"""
	class Solution(object):
	    def copyRandomList(self, head):
	        """
	        :type head: Node
	        :rtype: Node
	        """
	        def func(root):
	            if not root:
	                return None
	            if root in dict_all:
	                return dict_all[root]
	            new = Node(root.val)
	            dict_all[root] = new
	            new.next = func(root.next)
	            new.random = func(root.random)
	            return new
	        dict_all = {}
	        return func(head)


# 37
	# 序列化与反序列化。既可以用二叉树的前序遍历，也可以用二叉树的层序遍历。两种方法的解码方式不同。
	# 层序遍历的解码类似于队列的方法。
	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None

	class Codec:

	    def serialize(self, root):
	        """Encodes a tree to a single string.
	        
	        :type root: TreeNode
	        :rtype: str
	        """
	        if not root:
	            return ''
	        res,stack = [],[root]
	        while(stack):
	            now = stack.pop()
	            if not now:
	                res.append('None')
	                continue
	            res.append(str(now.val))
	            stack = [now.right,now.left]+stack
	        return ','.join(res)
	            
	    def deserialize(self, data):
	        """Decodes your encoded data to tree.
	        
	        :type data: str
	        :rtype: TreeNode
	        """
	        if not data:
	            return None
	        list_data = data.split(',')
	        root = TreeNode(list_data.pop(0))
	        list_my = [root]
	        while(list_my):
	            now = list_my.pop(0)
	            if not now: continue
	            left = list_data.pop(0)
	            right = list_data.pop(0)
	            now.left = TreeNode(left) if left!='None' else None
	            now.right = TreeNode(right) if right!='None' else None
	            list_my.append(now.left)
	            list_my.append(now.right)
	        return root



	    #     list_data = data.split(',')
	    #     return self.func(list_data)

	    # def func(self,list_data):
	    #     now = list_data.pop(0)
	    #     if now=='None':
	    #         return None
	    #     root = TreeNode(now)
	    #     root.left = self.func(list_data)
	    #     root.right = self.func(list_data)
	    #     return root
	        

	# Your Codec object will be instantiated and called as such:
	# codec = Codec()
	# codec.deserialize(codec.serialize(root))


# 38
	class Solution(object):
	    def permutation(self, s):
	        """
	        :type s: str
	        :rtype: List[str]
	        """
	        if len(s)==1:
	            return [s]
	        res = set()
	        for i in range(len(s)):
	            sub = self.permutation(s[:i]+s[i+1:])
	            for j in sub:
	                res.add(s[i]+j)
	        return list(res)

# 39
	# 摩尔投票发
	class Solution(object):
	    def majorityElement(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: int
	        """
	        res,count = 0,0
	        for i in nums:
	            if count == 0:
	                res = i
	                count += 1
	            else:
	                if i==res:
	                    count += 1
	                else:
	                    count -=1
	        return res


# 40
	class Solution(object):
	    def getLeastNumbers(self, arr, k):
	        """
	        :type arr: List[int]
	        :type k: int
	        :rtype: List[int]
	        """
	        self.quicksort(arr,0,len(arr)-1,k)
	        return sorted(arr[:k])

	    def quicksort(self,nums,i,j,k):
	        if i<j:
	            base = nums[i]
	            start,end = i,j
	            while(start<end):
	                while(start<end and nums[end]>base):
	                    end -= 1
	                nums[start] = nums[end]
	                while(start<end and nums[start]<=base):
	                    start += 1
	                nums[end]= nums[start]
	            nums[start] = base
	            left = start-i+1
	            if left<k:
	                self.quicksort(nums,start+1,j,k-left)
	            elif left>k:
	                self.quicksort(nums,i,start-1,k)

# 41
	# 数据流中的中位数。用大小顶推的做法。其中大顶堆维护的是数组的左半部分，小顶堆维护的是数组的右半部分。那么当两者长度相同，
	# 则取大小顶堆的头结点来平均，如果不相同则取小顶堆头部节点。注意，大顶堆是要变负号的。
	class MedianFinder(object):

	    def __init__(self):
	        """
	        initialize your data structure here.
	        """
	        self.hmax = []
	        self.hmin = []

	    def addNum(self, num):
	        """
	        :type num: int
	        :rtype: None
	        """
	        if len(self.hmax)==len(self.hmin):
	            heapq.heappush(self.hmax,-num)
	            h_max = heapq.heappop(self.hmax)
	            heapq.heappush(self.hmin,-h_max)
	        else:
	            heapq.heappush(self.hmin,num)
	            h_min = heapq.heappop(self.hmin)
	            heapq.heappush(self.hmax,-h_min)


	    def findMedian(self):
	        """
	        :rtype: float
	        """
	        if len(self.hmax)==len(self.hmin):
	            return (-self.hmax[0]+self.hmin[0])/2.0
	        else:
	            return self.hmin[0]



	# Your MedianFinder object will be instantiated and called as such:
	# obj = MedianFinder()
	# obj.addNum(num)
	# param_2 = obj.findMedian()


# 42
	class Solution(object):
	    def maxSubArray(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: int
	        """
	        res = [0]*len(nums)
	        res[0] = nums[0]
	        for i in range(1,len(nums)):
	            res[i] = nums[i] if res[i-1]<=0 else res[i-1]+nums[i]
	        return max(res)

# 43
    # 统计位1的个数。三个方程，当前位为0，那么height*digit, 当前位为1，那么height*digit+low+1, 当前位为其他，那么(height+1)*digit
	class Solution(object):
	    def countDigitOne(self, n):
	        """      
	        :type n: int
	        :rtype: int
	        """
	        sn = str(n)[::-1]
	        res = 0
	        for i in range(len(sn)):
	            digit = 10**i
	            height,low = sn[i+1:][::-1],sn[:i][::-1]
	            if not height: height = 0
	            if not low: low = 0
	            if sn[i]=='0':
	                res += int(height)*digit
	            elif sn[i]=='1':
	                res += int(height)*digit+int(low)+1
	            else:
	                res += (int(height)+1)*digit
	        return res 

# 44
	class Solution(object):
	    def findNthDigit(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        if n<10:
	            return n
	        n = n-9
	        k = 1
	        while(n>9*(10**k)*(k+1)):
	            n = n - 9*(10**k)*(k+1)
	            k += 1
	        idx1 = n/(k+1)
	        idx2 = n%(k+1)
	        num = 10**k+idx1
	        if idx2==0:
	            return int(str(num-1)[-1])
	        return int(str(num)[idx2-1])


# 45
	# 可以组成的最小数字，通过nums[i]+nums[j]和nums[j]+nums[i]比较大小来判断谁在谁前面进行排序即可。
	class Solution(object):
	    def minNumber(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: str
	        """
	        nums = map(str,nums)
	        self.quicksort(nums,0,len(nums)-1)
	        return ''.join(nums)
	    
	    def quicksort(self,nums,start,end):
	        if start<end:
	            i,j = start,end
	            base = nums[i]
	            while(i<j):
	                while(i<j and int(nums[j]+base)>int(base+nums[j])):
	                    j -= 1
	                nums[i] = nums[j]
	                while(i<j and int(nums[i]+base)<=int(base+nums[i])):
	                    i += 1
	                nums[j] = nums[i]
	            nums[i] = base
	            self.quicksort(nums,start,i-1)
	            self.quicksort(nums,j+1,end)

# 46
	class Solution(object):
	    def translateNum(self, num):
	        """
	        :type num: int
	        :rtype: int
	        """
	        num = str(num)
	        res = [0]*len(num)
	        res[0] = 1
	        for i in range(1,len(num)):
	            if int(num[i-1]+num[i])<26 and num[i-1]!='0':
	                if i==1: 
	                    res[i] = res[i-1]+1
	                else:
	                    res[i] = res[i-1]+res[i-2]
	            else:
	                res[i] = res[i-1]
	        return res[-1]


# 47
	class Solution(object):
	    def maxValue(self, grid):
	        """
	        :type grid: List[List[int]]
	        :rtype: int
	        """
	        len_x,len_y = len(grid),len(grid[0])
	        res = [[0 for i in range(len_y)] for j in range(len_x)]
	        res[0][0] = grid[0][0]
	        for i in range(len_x):
	            for j in range(len_y):
	                if i==0 and j==0: continue
	                if i==0:
	                    res[i][j] = res[i][j-1]+grid[i][j]
	                elif j==0:
	                    res[i][j] = res[i-1][j]+grid[i][j]
	                else:
	                    res[i][j] = max(res[i][j-1],res[i-1][j])+grid[i][j]
	        return res[-1][-1]


# 48
	class Solution(object):
	    def nthUglyNumber(self, n):
	        """
	        :type n: int
	        :rtype: int
	        """
	        i,j,k = 0,0,0
	        res = [1]
	        dict_res = {}
	        while(len(res)<n):
	            now = min(res[i]*2,res[j]*3,res[k]*5)
	            if now == res[i]*2:
	                i += 1
	            elif now == res[j]*3:
	                j += 1
	            else:
	                k += 1
	            if now not in dict_res:
	                res.append(now)
	                dict_res[now] = 1
	        return res[-1]
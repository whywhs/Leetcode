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
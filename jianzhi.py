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
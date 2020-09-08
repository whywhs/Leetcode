1. 两数之和
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
            dict_all[nums[i]] = i

2. 两数相加
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        res,flag = None,0
        while(l1 or l2):
            if not l1:
                num = l2.val
            elif not l2:
                num = l1.val
            else:
                num = l1.val+l2.val
            if flag==1:
                num +=1
            flag = 0
            if num>=10:
                num -= 10
                flag = 1
            now = ListNode(num)
            now.next = res
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            res = now
        if flag==1:
            new = ListNode(1)
            new.next = res
            res = new
        new = None
        while(res):
            res.next,res,new = new,res.next,res
        return new

3. 寻找两个正序数组的中位数
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        n1,n2 = len(nums1),len(nums2)
        if not n1:
            return nums2[n2//2] if n2%2!=0 else (nums2[n2//2]+nums2[n2//2-1])/2.0
        i,j = 0,n1
        while(i<=j):
            left = (i+j)//2
            right = (n1+n2+1)//2-left
            a1 = float('-inf') if left==0 else nums1[left-1]
            a2 = float('inf') if left==n1 else nums1[left]
            a3 = float('-inf') if right==0 else nums2[right-1]
            a4 = float('inf') if right==n2 else nums2[right]

            if max(a1,a3)<=min(a2,a4):
                break
            if a1>a4:
                j = left-1
            if a2<a3:
                i = left+1
        return max(a1,a3) if (n1+n2)%2==1 else (max(a1,a3)+min(a2,a4))/2.0


4.无重复字符的最长子串
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len,len_now = 1,1
        i,j = 0,1
        dict_all = {s[0]:1}
        while(i<j and j<len(s)):
            if s[j] in dict_all:
                if len_now > max_len:
                    max_len = len_now
                while(s[j] in dict_all):
                    dict_all.pop(s[i])
                    i += 1
                    len_now -= 1
            dict_all[s[j]] = 1
            j += 1
            len_now += 1
        return max_len if len_now<max_len else len_now


5. 最长回文子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def func(a,b):
            while(a>=0 and b<len(s) and s[a]==s[b]):
                a -= 1
                b += 1
            return a+1,b-1

        if len(s)<2:
            return s
        max_len = 0
        for i in range(1,len(s)):
            s1,e1 = func(i,i)
            if e1-s1+1>max_len:
                max_len = e1-s1+1
                res = s1
            s2,e2 = func(i-1,i)
            if e2-s2+1>max_len:
                max_len = e2-s2+1
                res = s2
        return s[res:res+max_len]


6. 整数反转
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        s = str(x)
        s = s[::-1]
        zero = 0
        while(s[zero]=='0'):
            zero += 1
        s = s[zero:]
        if s[-1]=='-':
            s = s[:len(s)-1]
            s = '-'+s
        return int(s) if -2**31<=int(s)<=2**31-1 else 0


7.字符串转换整数 (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        zero = 0
        while(zero<len(s) and s[zero]==' '):
            zero += 1
        s = s[zero:]
        if not s:
            return 0
        flag = 1
        if s[0] in '+-' or s[0].isdigit():
            if s[0] in '+-':
                if s[0] == '-':
                    flag = -1
                s = s[1:]
            digit = 0
            while(digit<len(s) and s[digit].isdigit()):
                digit += 1
            s = s[:digit]
            if not s:
                return 0
            if int(s)*flag>2**31-1: return 2**31-1
            elif int(s)*flag<-2**31: return -2**31
            return int(s)*flag
        return 0


8. 正则表达式匹配
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dict_all = {}
        def func(s,p):
            if not p and not s:
                return True
            elif not p:
                return False
            if (p,s) in dict_all:
                return dict_all[(p,s)]
            first = True if s and (p[0]==s[0] or p[0]=='.') else False
            if len(p)>1 and p[1]=='*':
                res = (first and func(s[1:],p)) or func(s,p[2:])
            else:
                res = func(s[1:],p[1:]) if first else False
            dict_all[(p,s)] = res
            return res
        
        return func(s,p)


9.盛最多水的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_now = 0
        i,j = 0,len(height)-1
        while(i<j):
            if height[i]<=height[j]:
                now = height[i]*(j-i)
                if now>max_now:
                    max_now = now
                i += 1
            else:
                now = height[j]*(j-i)
                if now>max_now:
                    max_now = now
                j -= 1
        return max_now


10. 罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_all = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res,flag = 0,0
        for i in range(len(s)):
            if flag==1:
                flag = 0
                continue
            if s[i]=='I':
                if i+1<len(s) and s[i+1] in 'VX':
                    res += 4 if s[i+1]=='V' else 9
                    flag = 1
                else:
                    res += 1
            elif s[i]=='X':
                if i+1<len(s) and s[i+1] in 'LC':
                    res += 40 if s[i+1]=='L' else 90
                    flag = 1
                else:
                    res += 10
            elif s[i]=='C':
                if i+1<len(s) and s[i+1] in 'DM':
                    res += 400 if s[i+1]=='D' else 900
                    flag = 1
                else:
                    res += 100
            else:
                res += dict_all[s[i]]
        return res       

11.最长公共前缀
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def judge(idx):
            now = strs[0][:idx+1]
            return all([strs[i][:idx+1]==now for i in range(1,len(strs))])


        if not strs:
            return ''
        min_len = min([len(s) for s in strs])
        i,j = 0,min_len-1
        while(i<=j):
            mid = (i+j)//2
            if judge(mid):
                i = mid+1
            else:
                j = mid-1
        return strs[0][:i]


12.三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j,k = i+1,len(nums)-1
            while(j<k):
                now = nums[i]+nums[j]+nums[k]
                if now==0:
                    res.append([nums[i],nums[j],nums[k]])
                    while(j+1<len(nums) and nums[j+1]==nums[j]):
                        j += 1
                    j += 1
                elif now>0:
                    k -= 1
                else:
                    j += 1
        return res

13. 电话号码组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_all = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def func(digits):
            if not digits:
                return ['']
            now = digits[-1]
            res = func(digits[:len(digits)-1])
            res_now = []
            for i in res:
                for j in dict_all[now]:
                    res_now.append(i+j)
            return res_now
        if not digits:
            return []
        return func(digits)

14.删除链表的倒数第N个节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow,fast = head,head
        while(n>0):
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while(fast):
            fast = fast.next
            if not fast:
                slow.next = slow.next.next
                break
            slow = slow.next
        return head

15. 有效的括号
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True
        dict_all = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if stack and stack[-1]==dict_all[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


16.合并两个有序链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        head1 = l1
        while(l1 and l2):
            while(l1 and l2 and l1.val<=l2.val):
                pre = l1
                l1 = l1.next
            pre.next = l2
            while(l1 and l2 and l1.val>l2.val):
                pre = l2
                l2 = l2.next
            if l1: pre.next = l1
        return head1


17.括号生成
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict_all = {}

        def func(n):
            if n==1:
                return ['()']
            res = func(n-1)
            res_now = []
            for i in res:
                for j in range(len(i)):
                    now = i[:j]+'()'+i[j:]
                    if now not in dict_all:
                        res_now.append(now)
                        dict_all[now] = 1
            return res_now

        return func(n)

18.删除排序数组中的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        res,k = 0,0
        for i in nums:
            if i in s:
                continue
            else:
                s[i] = 1
                res += 1
                nums[k] = i
                k += 1
        return res

19.两数相除
# 如果要扩大两倍，直接将该数左移一维即可，左移是后面补0。右移的话就是直接移除，最后为0。
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = -1 if (dividend<0)^(divisor<0) else 1
        dividend,divisor = abs(dividend),abs(divisor)

        res = 0
        while(divisor<=dividend):
            temp,i = divisor,1
            while(temp<=dividend):
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if flag == -1: res = -res
        return min(max(res,-2**31),2**31-1)


20.搜索旋转排序数组
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j = 0,len(nums)-1
        while(i<=j):
            mid = (i+j)//2
            if nums[mid] == target:
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

21.在排序数组中查找元素的第一个和最后一个位置
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(nums)-1
        while(i<=j):
            mid = (i+j)//2
            if nums[mid]>target:
                j = mid-1
            elif nums[mid]<target:
                i = mid+1
            else:
                if nums[i]==nums[j]==target:
                    return [i,j]
                elif nums[i]==target:
                    j -= 1
                elif nums[j]==target:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return [-1,-1]

22. 有效的数独
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        axis = {i:[] for i in range(9)}
        sub = [[],[],[]]
        for i in range(9):
            k = 0
            axis_i = {}
            for j in range(9):
                now = board[i][j]
                if now!='.':
                    if now in axis[j] or now in axis_i or now in sub[k]:
                        return False
                    axis_i[now] = 1
                    axis[j].append(now)
                    sub[k].append(now)
                if (j+1)%3==0:
                    k += 1
            if (i+1)%3==0:
                sub = [[],[],[]]
        return True

23. 外观数列
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        res = self.countAndSay(n-1)
        res_now = ''
        count,now = 1,res[0]
        for i in res[1:]:
            if i==now:
                count += 1
            else:
                res_now += str(count)+now
                now = i
                count = 1
        res_now += str(count)+now
        return res_now
        

24.缺失的第一个正数
# 这个题两个大坑，一个是不能够用python的a,b = b,a来进行交换，因为我需要交换的的索引套索引，这个索引在为交换的时候，还是原始值
# 另外一个就是循环条件的判断，nums[i]!=nums[nums[i]-1]和i!=nums[i]-1不一样的，前一种比后面的多了数值相等这种情况，即索引不同，但是
# 数值相同。
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while(i<len(nums)):
            while(1<=nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]):
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
            i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

25.
26.
27. 全排列
	class Solution(object):
	    def permute(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: List[List[int]]
	        """
	        if len(nums)==1:
	            return [nums]
	        res_now = []
	        for i in range(len(nums)):
	            res = self.permute(nums[:i]+nums[i+1:])
	            for j in res:
	                res_now.append(j+[nums[i]])
	        return res_now

28. 旋转图像
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        dict_all = {}
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if (i,j) and (j,i) not in dict_all:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                    dict_all[(i,j)] = 1
                    dict_all[(j,i)] = 1
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]

29.字母异位词分组
# 这个说了是小写字母的，所以就可以直接用一个26个英文字母的数组来作为idx即可。
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word = {}
        for i in strs:
            s = [0 for _ in range(26)]
            for j in i:
                s[ord(j)-ord('a')] += 1
            idx = ''.join(map(str,s))
            if idx in word:
                word[idx].append(i)
            else:
                word[idx] = [i]
        
        return [word[i] for i in word]

30. Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        flag = 0
        if n<0:
            flag = 1
            n = -n
        res = self.myPow(x,n//2)
        res *= res
        if n%2 != 0:
            res *= x
        return 1.0/res if flag==1 else res

31. 最大子序和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)

32. 螺旋矩阵
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while(matrix):
            res += matrix.pop(0)
            matrix = zip(*matrix)[::-1]
        return res


33. 跳跃游戏
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j,max_now = 0,0
        while(j<=max_now and max_now<len(nums)-1):
            if nums[j]+j>max_now:
                max_now = nums[j]+j
            j += 1
        if max_now>=len(nums)-1:
            return True
        return False


34. 合并区间
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        stack = [intervals[0]]
        i = 1
        while(i<len(intervals)):
            now = intervals[i]
            if stack[-1][0]<=now[0]<=stack[-1][1]:
                stack[-1][1] = max(stack[-1][1],now[1])
            else:
                stack.append(now)
            i += 1
        return stack

35. 不同路径
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    res[i][j] = 1
                    continue
                if i==0:
                    res[i][j] = res[i][j-1]
                elif j==0:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = res[i-1][j]+res[i][j-1]
        return res[-1][-1]

36.加一
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                digits[i] += 1
            digits[i] += flag
            flag = 0
            if digits[i]>=10:
                digits[i] -= 10
                flag = 1 
        if flag==1:
            digits = [1]+digits
        return digits

37. x 的平方根
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # i,j,res = 0,x,-1
        # while(i<=j):
        #     mid = (i+j)//2
        #     if mid**2>x:
        #         j = mid-1
        #     elif mid**2<=x:
        #         res = mid
        #         i = mid+1
        # return res
        if x==0: return 0
        m,x_now = float(x),float(x)
        while(True):
            x_next = 0.5*(x_now+m/x_now)
            if x_now-x_next<1e-7:
                return int(x_now)
            x_now = x_next

38. 爬楼梯
class Solution(object):
    def __init__(self):
        self.dict_all = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        if n not in self.dict_all:
            self.dict_all[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dict_all[n]



39. 矩阵置零
# 这个算法一定要记住，是从右下往左上。
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0:
                    if matrix[i][j]==0:
                       first = True
                else:
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        for i in range(len(matrix)-1,0,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0


40. 颜色分类
# 这个题目最简单的方法思路还是很巧妙地。定义三个指针，分别是i,j,k。其中i代表i左侧的所有数都是0，k代表k右侧的数都是2.j是一个移动位。
# 解决的方法就是，j在数组上滑动，如果j是2，那么j就可以和k进行交换，就可以保证k一定是2，也就可以k-1.
# 如果j是1，那么就直接将j+1即可。
# 如果j是0, 那么就需要将j和i进行交换，则i+1即可。同时，j也要加1，j+1这里很关键，因为如果j和i进行交换，那么i缓过来的数一定是j已经扫描过得
# 数。同时，还可以避免j和i之间，j《i的现象出现。如果出现这种现象，那么j将一直为0，整个序列也就错误了。
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j,k = 0,0,len(nums)-1
        while(j<=k):
            while(j<=k and nums[j]==2):
                nums[j],nums[k] = nums[k],nums[j]
                k -= 1
            while(j<=k and nums[j]==0):
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            while(j<=k and nums[j]==1):
                j += 1

41.

42.子集
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.func(nums)
        return res+[[]]
    
    def func(self,nums):
        if len(nums)==1:
            return [nums]
        res = self.func(nums[1:])
        res_now = []
        for i in res:
            res_now.append([nums[0]]+i)
        return res+res_now+[[nums[0]]]

43. 单词搜索
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def func(x,y,k):
            if x>=0 and y>=0 and x<len(board) and y<len(board[0]) and board[x][y]==word[k]:
                if k==len(word)-1:
                    return True
                temp = board[x][y]
                board[x][y] = '-1'
                if func(x-1,y,k+1) or func(x+1,y,k+1) or func(x,y-1,k+1) or func(x,y+1,k+1):
                    return True
                board[x][y] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and func(i,j,0):
                    return True
        return False

44.

45. 合并两个有序数组。 这个是在nums1中空出了足够的空间来填入nums2
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return 
        if m==0:
            nums1[:n] = nums2[:n]
            return 
        i,j = m-1,n-1
        k = (m+n)-1
        while(i>=0 and j>=0):
            while(i>=0 and nums1[i]>nums2[j]):
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            if i==-1:
                nums1[:k+1] = nums2[:j+1]
                break
            while(j>=0 and nums1[i]<=nums2[j]):
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

46. 解码方法
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        res = [0]*len(s)
        res[0] = 1
        for i in range(1,len(s)):
            if 1<=int(s[i-1]+s[i])<=26:
                if s[i]=='0':
                    res[i] = res[i-2] if i!=1 else 1
                elif s[i-1]=='0':
                    res[i] = res[i-1]
                else:
                    res[i] = res[i-2]+res[i-1] if i!=1 else res[i-1]+1
            else:
                if s[i]=='0' and (int(s[i-1]+s[i])==0 or int(s[i-1]+s[i])>26):
                    return 0
                res[i] = res[i-1]
        return res[-1]


47. 二叉树中序遍历（迭代）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack,res = [],[]
        while(root):
            stack.append(root)
            root = root.left
        while(stack):
            now = stack.pop()
            res.append(now.val)
            if now.right:
                now = now.right
                while(now):
                    stack.append(now)
                    now = now.left
        return res


48. 验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        while(root):
            stack.append(root)
            root = root.left
        while(stack):
            now = stack.pop()
            val = now.val
            if now.right:
                now = now.right
                while(now):
                    stack.append(now)
                    now = now.left
            if stack and val>=stack[-1].val:
                return False
        return True

49. 对称二叉树
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
        if not root:
            return True
        return self.judge(root.left,root.right)
    
    def judge(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val==right.val:
            return self.judge(left.left,right.right) and self.judge(left.right,right.left)
        return False

50. 二叉树层序遍历
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
        self.func(root,res,0)
        return res
        
    def func(self,root,res,k):
        if not root:
            return
        if k==len(res):
            res.append([])
        res[k].append(root.val)
        self.func(root.left,res,k+1)
        self.func(root.right,res,k+1)

51. 二叉树深度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        high,sub = 1,[]
        while(stack):
            now = stack.pop()
            if now.left:
                sub.append(now.left)
            if now.right:
                sub.append(now.right)
            if not stack:
                if sub: high += 1
                stack = sub
                sub = []
        return high

52. 从前序与中序遍历序列构造二叉树
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
        root = TreeNode(now)
        idx = inorder.index(now)
        root.left = self.buildTree(preorder[:idx],inorder[:idx])
        root.right = self.buildTree(preorder[idx:],inorder[idx+1:])
        return root

53. 填充每个节点的下一个右侧节点指针
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        self.func(root)
        return root

    def func(self,root):
        left,right = root.left,root.right
        if left:
            left.next = right
            right.next = root.next.left if root.next else None
            self.func(root.left)
            self.func(root.right)


54. 二叉树中的最大路径和
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def func(root):
            if not root.left and not root.right:
                return root.val,root.val
            if not root.left or not root.right:
                left = root.left or root.right
                left,res_l = func(left)
                return max(left+root.val,root.val),max(left,res_l,left+root.val,root.val)
            else:
                left,res_l = func(root.left)
                right,res_r = func(root.right)
                return max(max(left,right),0)+root.val,max(left,right,res_l,res_r,left+right+root.val)
        
        return max(func(root))

55. 验证回文串
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [ch.lower() for ch in s if ch.isalnum()]
        if not s: return True
        i,j = 0,len(s)-1
        while(i<j and s[i]==s[j]):
            i += 1
            j -= 1
        return True if i>=j else False

56. 单词接龙
# 这个可以采用'*ab','g*b'
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word = {}
        for i in wordList:
            for j in range(len(i)):
                s = i[:j]+'*'+i[j+1:]
                if s in word:
                    word[s].append(i)
                else:
                    word[s] = [i]
        
        count = 1
        dict_all = {}
        begin,sub = [beginWord],[]
        while(begin):
            begin_word = begin.pop()
            for i in range(len(begin_word)):
                now = begin_word[:i]+'*'+begin_word[i+1:]
                if now in word and now not in dict_all:
                    if endWord in word[now]:
                        return count+1
                    sub += word[now]
                    dict_all[now] = 1
            if not begin:
                count += 1
                begin = sub
                sub = []
        return 0

57. 最长连续序列 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dict_all = {}
        for i in nums:
            dict_all[i] = 1
        res,max_res = 1,1
        for i in nums:
            if i-1 not in dict_all:
                while(i+1 in dict_all):
                    i += 1
                    res += 1
                if res>max_res:
                    max_res = res
                res = 1
        return max_res

58. 朋友圈（并查集）
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        res,visit = 0,set()
        for i in range(n):
            if i not in visit:
                sub = [i]
                while(sub):
                    now = sub.pop()
                    for j in range(n):
                        if M[now][j] and j not in visit:
                            visit.add(j)
                            sub.append(j)
                res += 1
        return res

59. 分割回文串
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        if len(s)==1:
            return [[s]]
        res_now = []
        for i in range(1,len(s)+1):
            if s[:i]==s[:i][::-1]:
                next_res = self.partition(s[i:])
                for j in next_res:
                    j = [s[:i]]+j
                    res_now.append(j)
        return res_now


60. 加油站
# 这个是可以直接一次遍历给出来结果的。
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        v = []
        for i in range(len(gas)):
            v.append(gas[i]-cost[i])
        v *= 2
        i = 0
        while(i<len(gas)):
            if v[i]<0:
                i += 1
            else:
                j,sum_now = i,0
                while(j-i<len(gas)):
                    sum_now += v[j]
                    if sum_now<0:
                        break
                    j += 1
                if sum_now>=0:
                    return i
                i = j+1
        return -1

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
61. 复杂链表复制
class Solution(object):
    def __init__(self):
        self.flag = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        if head in self.flag:
            return self.flag[head]
        new = Node(head.val)
        self.flag[head] = new
        new.random = self.copyRandomList(head.random)
        new.next = self.copyRandomList(head.next)
        return new

62. 单词拆分
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dict_all = {}
        for i in wordDict:
            word = dict_all
            for j in i:
                word[j] = word.setdefault(j,{})
                word = word[j]
            word['end'] = True

        stack = [0]
        while(stack):
            i = stack.pop()
            word = dict_all
            while(i<len(s) and s[i] in word):
                word = word[s[i]]
                if 'end' in word:
                    if i==len(s)-1:
                        return True
                    stack.append(i+1)
                i += 1
        return False

63.环形链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow,fast = head,head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

64. 排序链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow,fast = head,head
        pre = None
        while(slow and fast and fast.next):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if not pre:
            return head
        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        if not left or not right:
            return left or right
        if left.val>right.val:
            left,right = right,left
        a,b = left,right
        pre = None
        while(a and b):
            while(a and b and a.val<=b.val):
                pre = a
                a = a.next
            pre.next = b
            while(a and b and a.val>b.val):
                pre = b
                b = b.next
            if a: pre.next = a
        return left


65. 逆波兰表达式求值
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            try:
                now = int(tokens[i])
                stack.append(now)
            except:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i]=='+':
                    stack.append(b+a)
                elif tokens[i]=='-':
                    stack.append(b-a)
                elif tokens[i]=='*':
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
        return stack[-1]


66.乘积最大子数组
# 这个题目的思路很巧妙。直接一次遍历就可以得到结果。方法就是在遍历的过程中记录两个值分别是最小值
# 和最大值。之所以记录这两个值是因为最小值*当前值很有可能变成最大值。
# 同时还需要注意一点就是，pre——max不能直接更新，因为它在下面还被用到了。
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_max,pre_min = 1,1
        res = float('-inf')
        for i in range(len(nums)):
            now_pre_max = max(nums[i],nums[i]*pre_max,nums[i]*pre_min)
            now_pre_min = min(nums[i],nums[i]*pre_max,nums[i]*pre_min)
            pre_max = now_pre_max
            pre_min = now_pre_min
            if pre_max>res:
                res = pre_max
        return res


67.最小栈
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mylist1 = []
        self.mylist2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.mylist1.append(x)
        if not self.mylist2:
            self.mylist2.append(x)
        else:
            if x<self.mylist2[-1]:
                self.mylist2.append(x)
            else:
                self.mylist2.append(self.mylist2[-1])

    def pop(self):
        """
        :rtype: None
        """
        if self.mylist1:
            self.mylist1.pop()
            self.mylist2.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.mylist1[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.mylist2[-1]

68. 相交链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        a,b = headA,headB
        while(a!=b):
            a = a.next
            b = b.next
            if not a and not b:
                return None
            if not a:
                a = headB
            if not b:
                b = headA
        return a


69. 寻找峰值
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        if nums[0]>nums[1]: return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        i,j = 0,len(nums)-1
        while(i<=j):
            mid = (i+j)//2
            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            if nums[mid-1]>nums[mid]:
                j = mid-1
            elif nums[mid+1]>nums[mid]:
                i = mid+1
        return 

70. 分数到小数
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator==0:
            return '0'
        flag = 1
        if numerator*denominator<0:
            flag = -1
        numerator,denominator = abs(numerator),abs(denominator)
        res = '' if flag==1 else '-'
        k,dict_my = 0,{}
        while(True):
            a = numerator//denominator
            res += str(a)
            numerator -= denominator*a
            if numerator==0:
                return res
            if k==0: 
                res += '.'
                k += 1
            numerator *= 10
            if numerator in dict_my:
                return res[:dict_my[numerator]]+'('+res[dict_my[numerator]:]+')'
            dict_my[numerator] = len(res)

71. 多数元素 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,time = nums[0],1
        for i in range(1,len(nums)):
            if a==nums[i]:
                time += 1
            else:
                time -= 1
                if time==0:
                    a = nums[i+1]
        return a

72. Excel表列序号
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = {chr(s):s-ord('A')+1 for s in range(ord('A'),ord('Z')+1)}
        res = 0
        for i in range(len(s)):
            res += word[s[-i-1]]*(26**i)
        return res

73. 阶乘后的零
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while(n>=5):
            n /= 5
            res += n
        return res

74. 最大数
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str,nums)
        self.quicksort(nums,0,len(nums)-1)
        return '0' if nums[-1]=='0' else ''.join(nums[::-1])
    
    def quicksort(self,nums,start,end):
        i,j = start,end
        if i<j:
            base = nums[i]
            while(i<j):
                while(i<j and int(base+nums[j])<=int(nums[j]+base)):
                    j -= 1
                nums[i] = nums[j]
                while(i<j and int(nums[i]+base)<int(base+nums[i])):
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            self.quicksort(nums,start,i-1)
            self.quicksort(nums,j+1,end)

75. 旋转数组
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end):
            mid = (end-start+1)//2
            for i in range(mid):
                nums[start+i],nums[end-i] = nums[end-i],nums[start+i]
        
        if len(nums)<2:
            return nums
        k = k%(len(nums))
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

76. 颠倒二进制位
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        len_now = 32-len(b)
        b = '0'*len_now+b
        res = 0
        for i in range(len(b)):
            res += int(b[i])*(2**i)
        return res

77. 位1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while(n):
            if n%2==1:
                res += 1
            n >>= 1
        return res

78. 打家劫舍
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums)==1: return nums[0]
        res = [0]*len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            res[i] = max(res[i-1],res[i-2]+nums[i])
        return res[-1]

79. 岛屿数量
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    stack = [(i,j)]
                    while(stack):
                        x,y = stack.pop()
                        if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]=='1':
                            grid[x][y] = '2'
                            stack += [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
                    res += 1
        return res

80. 计数质数
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        flag,count = {},0
        right = int(n**0.5)+1
        for i in range(2,right):
            if i in flag:
                continue
            k = 2
            while(i*k<n):
                now = i*k
                k += 1
                if now not in flag:
                    flag[now] = 1
                    count += 1
        return n-2-count

81. 前缀树
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        now = self.tree
        for i in word:
            now[i] = now.setdefault(i,{})
            now = now[i]
        now['end']=True 


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        now = self.tree
        for i in word:
            if i in now:
                now = now[i]
            else:
                return False
        return True if 'end' in now else False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        now = self.tree
        for i in prefix:
            if i in now:
                now = now[i]
            else:
                return False
        return True

82. 数组中的第K个元素
# 这个的关键在于建堆操作。这里要学习一下，建堆是从底向上进行的。对于数组nums来说，建堆
# 操作只需要从len(nums)//2-1这个地方开始即可。因为这个的子节点就是最后一个数。
# 同时，对这个数进行左右节点的判断。如果左右节点均比当前节点小，则终止。否则替换之后
# 还会继续对替换后的节点进行交换。
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 建堆过程
        def heapq(nums,start,end):
            max_now = start
            while(True):
                if start*2+1<=end and nums[start*2+1]>nums[max_now]:
                    max_now = start*2+1
                if start*2+2<=end and nums[start*2+2]>nums[max_now]:
                    max_now = start*2+2
                if max_now==start:
                    break
                nums[max_now],nums[start] = nums[start],nums[max_now]
                start = max_now
        
        # 只需要对len(nums)//2-1位置开始的数进行分步建堆即可。因为该数的2i+2就是len(nums)了
        for i in range(len(nums)//2-1,-1,-1):
            heapq(nums,i,len(nums)-1)

        while(k!=1):
            nums[0],nums[-1] = nums[-1],nums[0]
            nums.pop()
            heapq(nums,0,len(nums)-1)
            k -= 1
        return nums[0]

83. 基本计算器II
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack,i = [],0
        op = False
        flag = 1
        while(i<len(s)):
            if s[i]==' ':
                i += 1
                continue
            if s[i].isdigit():
                num = 0
                while(i<len(s) and (s[i].isdigit() or s[i]==' ')):
                    if s[i]==' ':
                        i += 1
                        continue
                    num = int(s[i])+num*10
                    i += 1
                if op=='*':
                    left = stack.pop()
                    stack.append(left*num)
                    op = False
                elif op=='/':
                    left = stack.pop()
                    stack.append(int(left/float(num)))
                    op = False
                else:
                    stack.append(num*flag)
            if i<len(s) and s[i] in '+-*/':
                if s[i]=='-':
                    flag = -1
                elif s[i]=='*':
                    op = '*'
                elif s[i]=='/':
                    op = '/'
                else:
                    flag = 1
            i += 1
        return sum(stack)

84. 二叉搜索树中第k小的元素
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while(root):
            stack.append(root)
            root = root.left
        while(stack):
            now = stack.pop()
            k -= 1
            if k==0:
                return now.val
            if now.right:
                now = now.right
                while(now):
                    stack.append(now)
                    now = now.left
        return 

85. 回文链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        if not head.next.next: return head.val==head.next.val
        slow,fast = head,head
        k = 0
        while(fast and fast.next):
            k += 1
            fast = fast.next.next
            pre = slow
            slow = slow.next
        new = self.reverse(slow)
        while(head and new and head.val==new.val):
            head = head.next
            new = new.next
        return False if head and new else True

    def reverse(self,head):
        new = None
        while(head):
            head.next,new,head = new,head,head.next
        return new

86. 二叉树的最近公共祖先
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        if root.val==p.val or root.val==q.val:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right

87. 删除链表中的节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


88. 除自身以外数组的乘积
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        res[0] = nums[0]
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i]
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                res[j] = res[j-1]
                now = nums[j]
            elif j==0:
                res[j] = now
            else:
                res[j] = res[j-1]*now
                now *= nums[j]
        return res


89. 滑动窗口最大值
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k==1: return nums
        idx,res = [0],[]
        min_now = [nums[0]]
        for i in range(1,len(nums)):
            if i-idx[0]==k:
                idx.pop(0)
                min_now.pop(0)
            while(min_now and nums[i]>min_now[-1]):
                min_now.pop()
                idx.pop()
            min_now.append(nums[i])
            idx.append(i)
            if i>=k-1:
                res.append(min_now[0])
        return res

90. 完全平方数
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1 if int(i**0.5)==i**0.5 else float('inf') for i in range(n+1)]
        for i in range(n+1):
            if res[i] == 1:
                continue
            else:
                j = 1
                while(j*j<=i):
                    res[i] = min(res[i-j*j]+1,res[i])
                    j += 1
        return res[-1]

91. 移动0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1


92. 寻找重复数
# 类似于一个龟兔赛跑的问题。求循环链表的入口节点。
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast = 0,0
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        new = 0
        while(new!=slow):
            slow = nums[slow]
            new = nums[new]
        return new

93. 生命游戏
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def count(i,j):
            stack = [(i,j+1),(i,j-1),(i+1,j),(i-1,j),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
            num = 0
            while(stack):
                x,y = stack.pop()
                if x>=0 and x<m and y>=0 and y<n and board[x][y]==1:
                    num += 1
            return True if num==3 or (num==2 and board[i][j]==1) else False

        def judge(i,j):
            flag = count(i,j)
            if j+1<n:
                judge(i,j+1)
            else:
                if i+1<m:
                    judge(i+1,0)
            board[i][j] = 1 if flag else 0
        
        m,n = len(board),len(board[0])
        if m and n:
            judge(0,0)


94. 最长上升子序列
# 这个题目的原理就相当于，如果本身数组是[a,b,c,d]，那么我新来了一个e。如果e可以进行替换，
# 那么就可以替换，这样，所有可以在之后append的数，无论对于e还是对于被替换的都是可以算上一个
# 长度的。即因为他是替换，而不是累加，这种做法就可以得到正确的长度。但是对于得到正确的序列，这种做法
# 是不可以的。
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = [nums[0]]
        max_len = 0
        for i in range(1,len(nums)):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                j,k = 0,len(res)-1
                while(j<k):
                    mid = (j+k)//2
                    if res[mid]>=nums[i]:
                        k = mid
                    else:
                        j = mid+1
                res[j] = nums[i]
        return len(res)
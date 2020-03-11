# 将数组分成和相等的三个部分。这个题目关键点就是在和除以3.然后进行while寻找，如果left为该值，则以left为起点继续寻找mid，直到找到为止。
# 需要注意的地方主要是，和的初值为0。如果和的初值为0，那么就会出现类似[1,-1,-1,1]这种错误，因为它的和1/3是0.所以初值最好是A[i]

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        sum_A = sum(A)/3
        if sum_A != int(sum_A):
            return False

        i = 0
        left = A[i]
        while(i<len(A)-3 and left!=sum_A):
            i = i+1
            left += A[i]

        if left!= sum_A: 
            return False
        
        j = i+1
        mid = A[i+1]
        while(j<len(A)-2 and mid!=sum_A):
            j = j+1
            mid += A[j]

        if mid!= sum_A:
            return False
        return True

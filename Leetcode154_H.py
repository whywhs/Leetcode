# 旋转数组的最小数字。 这个题目的O(N)做法是比较好想出来的，但是这个题目比较好的方法是采用二分法。
# 采用二分法的做法就是求中值，然后来进行判断。值得注意的就是在出现其他情况时，一定是j-=1，因为如果是i+=1的话，出来的会是大值。
# 具体原因就是，1、mid是由i+j//2算出来的，那么mid一定是偏向小的，如果用i+，结果就会是大的。
# 2、当是正常排列，那么j--的话，结果就会是到最小值，而i++的话，结果就会变成大值。
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers)==1:
            return numbers[0]

        i,j = 0,len(numbers)-1
        while(i<j):
            mid = (i+j)//2
            if numbers[mid]>numbers[j]:
                i = mid+1
            elif numbers[mid]<numbers[i]:
                j = mid
            else:
                j -= 1
        return numbers[i]


        # i = 1
        # while(i<len(numbers) and numbers[-i]>=numbers[-i-1]):
        #     i = i+1
        # if i==len(numbers):
        #     return numbers[0]
        # if i==1:
        #     return numbers[-1]

        # return numbers[-i]
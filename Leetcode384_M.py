#Fisher-Yates乱序法，是标准的打乱数组算法，可以使得打乱后的数组出现概率一样。做法：
#1、对数组从后往前进行检索
#2、在当前索引值前面的所有范围内，随机生成随机数。random.randint(a,b)
#3、交换当前索引与随机数的索引值
#for i from n-1 downto 0：//数组i从n-1到0循环执行n次
#        random_choice j <-- random integer such that 0 ≤j ≤i;//生成一个0到n-1之间的随机索引
#        exchange a[j] and a[i]  //将交换之后剩余的序列中最后一个元素与随机选取的元素交换

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        import copy
        
        nums_rand = copy.deepcopy(self.nums)
        for i in range(len(nums_rand)):
            a = -i-1
            b = random.randint(0,len(nums_rand)-i-1)
            nums_rand[a],nums_rand[b]=nums_rand[b],nums_rand[a]
            
        return nums_rand
       

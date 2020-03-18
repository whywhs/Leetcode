# 合并区间。 这个通过排序加遍历，来获得合并后的区间。
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        result = [intervals[0]]
        for i in intervals[1:]:
            if i[0]<=result[-1][1]:
                result[-1][1] = max(i[1],result[-1][1])
            else:
                result.append(i)
        return result 
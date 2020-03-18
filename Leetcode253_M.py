# 会议室II。 这个题目两种做法，其实最开始最关键的一步是先按开始时间的大小进行排序，这样之后做的步骤才都是有意义的。
# 具体做法上，我是用了遍历的方法，题解是用了最小堆。最小堆更简单也更快。
# 最小堆即保留最小的结束时间来作为查询的依据。如果当前会议开始时间大于最小堆最小的结束时间，那么就可以在同一个会议室进行。
# 否则，一定需要新开一个会议室来容纳。在操作上，如果新开会议室，那么久将新会议室的结束时间入堆，如果不需要新开会议室，就将
# 最小堆的最小值更新为新的会议的结束时间即可。
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)<2:
            return len(intervals)
        import heapq
        intervals.sort(key=lambda x:x[0])
        end = []
        heapq.heappush(end,intervals[0][1])
        for i in intervals[1:]:
            if i[0]>=end[0]:
                heapq.heappop(end)
                heapq.heappush(end,i[1])
            else:
                heapq.heappush(end,i[1])
        return len(end)

        """
        if intervals==[]:
            return 0
        intervals.sort(key=lambda x:x[0])
        list_all = [intervals[0]]
        flag,count = 0,1
        for i in intervals[1:]:
            len_l = len(list_all)
            for j in range(len_l):
                if not self.judge(i,list_all[j]):
                    flag = 1
                    list_all[j] = [list_all[j][0],i[1]]
                    break
            if flag==0:
                count += 1 
                list_all.append(i)
            flag = 0
        return count

    def judge(self,i,j):
        x_new = max(i[0],j[0])
        y_new = min(i[1],j[1])
        if y_new-x_new<=0:
            return False
        return True
        """
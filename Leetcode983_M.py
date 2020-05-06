# 最低票价。这个题目说是反向DP，但是正向的也是非常好做，这个题应该很容易解出来才对。
# 建立res来存储天数。那么当前的就是等于res[i-1],res[i-7],res[i-30]这三个里面加上cost之后的最小值。
# 如果i<7或者<30，那么只需要将该天定义为7和30的钱数即可。
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # res = [0]*400
        # if days[-1]==365:
        #     days.pop()
        #     res[365] = costs[0]
        # for i in range(364,0,-1):
        #     if days!=[] and i == days[-1]:
        #         days.pop()
        #         res[i] = min(res[i+1]+costs[0],res[i+7]+costs[1],res[i+30]+costs[2])
        #     else:
        #         res[i] = res[i+1]
        # return res[1]
        
        res = [0]*(days[-1]+1)
        k = 0
        for i in range(1,len(res)):
            if i!=days[k]:
                res[i] = res[i-1]
            else:
                a,b,c = costs[0],costs[1],costs[2]
                k += 1
                a = res[i-1]+costs[0]
                if i-7>=0:
                    b = res[i-7]+costs[1]
                if i-30>=0:
                    c = res[i-30]+costs[2]
                res[i] = min(a,b,c)
        return res[-1]

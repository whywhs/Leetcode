# 水壶问题。这个的最优解法还是需要好好思考才行。这个题从数学上来看是求最大公约数。
# 抽象出来就是 ax+by=z的求解问题。 这个问题求解的关键就是最大公约数。
# 求最大公约数的算法是辗转相除法，辗转相除法即反复除直到整除为止，则被整除的数即最大公约数。
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x+y < z:
            return False
        if x>y:
            x,y=y,x
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0

# 这个题目的正常解法就是做BFS，将所有的情况进行遍历。即维护一个stack，当stack内有数时，一直进行直到为空。
# 中间需要记录算过的数，即加入一个dict来进行记录。同时，对所有的可能情况进行分类，来一步一步向下走。
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """ 
        stack = [(0,0)]
        dict_my = {}
        while(stack!=[]):
            now = stack.pop()
            if now in dict_my:
                continue
            dict_my[now] = 1
            if now[0]==z or now[1]==z or now[0]+now[1]==z:
                return True

            stack.append((0,now[1])) #空x
            stack.append((now[0],0)) #空y
            stack.append((x,now[1])) #满x
            stack.append((now[0],y)) #满y
            x_new,y_new = min(now[0]+now[1],x),max(now[1]-x+now[0],0)
            stack.append((x_new,y_new)) #将y倒入x
            x_new,y_new = max(now[0]-y+now[1],0),min(now[0]+now[1],y)
            stack.append((x_new,y_new)) #将x倒入y
        return False
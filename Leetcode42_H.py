# 接雨水。这个题目需要考虑的情况比较多，我写的方法比较慢。
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        sub,i = [height[0]],1
        count = 0
        while(i<len(height)):
            while(i<len(height) and height[i]<=sub[-1]):
                sub.append(height[i])
                i = i+1
            if i==len(height): break
            sub.append(height[i])
            while(i+1<len(height)):
                if height[i+1]>height[i] or (height[i]<sub[0] and max(height[i+1:])>height[i]):
                    sub.append(height[i+1])
                    i += 1
                else: break
            num_count = self.my_count(sub)
            count += num_count if num_count>=0 else 0
            sub = [height[i]]
            i += 1
        return count
    

    def my_count(self,list_my):
        if len(list_my)<3:
            return 0
        k,j = 0,1
        while(k+1<len(list_my) and list_my[k+1]>=list_my[-1]):
            list_my.pop(k)
        while(j+1<=len(list_my) and list_my[-j-1]>=list_my[0]):
            list_my.pop()
        h = min(list_my[0],list_my[-1])
        w = len(list_my)
        size = (w-2)*h
        for i in list_my[1:len(list_my)-1]:
            size -= i
        return size
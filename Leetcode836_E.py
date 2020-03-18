# 矩形重叠。 一个简单的NMS问题，重叠即min-max看是否大于0即可。
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1_new = max(rec1[0],rec2[0])
        x2_new = min(rec1[2],rec2[2])
        y1_new = max(rec1[1],rec2[1])
        y2_new = min(rec1[3],rec2[3])

        if x2_new-x1_new>0 and y2_new-y1_new>0:
            return True
        return False
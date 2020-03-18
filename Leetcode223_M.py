# 矩形面积。这个题目就是一个只包含两个矩形的NMS，在求相交的基础上，减去相交的面积。如果不想交，则减0.
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        x11 = max(A,E)
        x22 = min(C,G)
        y11 = max(B,F)
        y22 = min(D,H)
        area3 = max((x22-x11),0)*max((y22-y11),0)
        return area1+area2-area3
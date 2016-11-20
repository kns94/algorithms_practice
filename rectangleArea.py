class Solution(object):

    def size(self, B, D):

        if (B >= 0 and D >= 0) or (B < 0 and D < 0):
            length = abs(abs(B) - abs(D))
        else:
            length = abs(B) + abs(D)

        """
        if (A >= 0 and C >= 0) or (A < 0 and C < 0):
            width1 = abs(abs(A) - abs(C))
        else:
            width1 = abs(A) + abs(C)

        return length1 * width1
        """
        return length

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
    
        area1 = self.size(B, D) * self.size(A, C)
        area2 = self.size(E, G) * self.size(F, H)
        
        if A <= E and E <= C and A <= G and G <= C and B <= F and F <= D and B <= H and H <= D:
            return area1


        common_area = 0
        common_length = 0
        common_width = 0 

        if (A <= E and E <= C):
            common_length = self.size(E, C)
        elif (A <= G and G <= C):
            common_length = self.size(A, H)

        if (B <= H and H <= D):
            common_width = self.size(B, H)
        elif (B <= E and E <= D):
            common_width = self.size(E, D)

        common_area = common_length * common_width
        return (area1 + area2 - common_area)

print Solution().computeArea(-2, -2, 2, 2, -1, -1, 1, 1)
#(-3, -0, 3, 4, 0, -1, 9, 2)
#(-2, -2, 2, 2, -1, -1, 1, 1)
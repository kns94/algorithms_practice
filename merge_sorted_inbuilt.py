class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return
        
        for i in range(n):
            nums1[m + i] = nums2[i]
         
           
        nums1.sort()
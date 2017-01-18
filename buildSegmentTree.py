import math

class NumArray(object):

    def __init__(self, arr):

        if len(arr) == 0:
            return None

        self.arr = arr
        self.segTree = [0] * int(2 * pow(2, math.ceil(math.log(len(self.arr), 2))) - 1)
        self.buildTree(0, len(self.arr) - 1, 0)
        #print self.segTree

    def buildTree(self, low, high, pos):
        '''
            Build the segment tree using recursion
        '''
        
        if low == high:
            #In case you cannot divide further, fill value in the tree
            self.segTree[pos] = self.arr[low]
        else:
            self.buildTree(low, (low + high)/2, 2 * pos + 1)
            self.buildTree((low + high)/2 + 1, high, 2 * pos + 2)
            self.segTree[pos] = self.segTree[2*pos + 1] + self.segTree[2*pos + 2]  
        return


    def checkRange(self, i, j, start, end, pos):
        '''
        Three conditions to check here:
            1. i&j are both inside start and end
            2. i&j are partially inside
            3. i&j are not in start and end
        '''

        print start, end, pos

        if i > end or j < start:
            return 0

        if i == j:
            #print 'base'
            return self.arr[i]
        elif start == i and end == j:
            #Same Tree required
            #print 'exact'
            return self.segTree[pos]
        elif start <= i and end >= j:
            #Completely engulfed
            #print 'engulfed'
            return self.checkRange(i, j, start, (start + end)/2, 2*start + 1) + self.checkRange(i, j, (start + end)/2 + 1, end, 2*start + 2)
        elif start == j:
            #Require only the first value
            #print 'j'
            return self.arr[j]
        elif end == i:
            #Require only the last value
            #print 'i'
            return self.arr[i]
        elif i <= start and j >= end:
            #Completely inside required value - return this directly
            #print 'caught'
            return self.segTree[pos]
        #elif (i >= start and i <= end and j >= end) or (i <= start and j >= start and j <= end):
            #partially engulfed
        #    return self.checkRange(i, j, start, (start + end)/2, 2*start + 1) + self.checkRange(i, j, (start + end)/2 + 1, end, 2*start + 2)
        #elif i <= start and j >= start and j <= end:
        #    return self.checkRange(i, j, start, (start + end)/2, 2*start + 1) 
        else:
            return self.checkRange(i, j, start, (start + end)/2, 2*start + 1) + self.checkRange(i, j, (start + end)/2 + 1, end, 2*start + 2)

    def sumRange(self, i, j):
        '''
            Now perform binary search on the tree - traverse based on index value
        '''

        if i > len(self.arr) or j < 0:
            return -1

        return self.checkRange(i, j, 0, len(self.arr) - 1, 0)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int

        Build segment tree when updating array
        """ 

        self.arr[i] = val
        self.buildTree(0, len(self.arr) - 1, 0)

if __name__ == "__main__":
    arr = [-28,-39,53,65,11,-56,-65,-39,-43,97]
    sol = NumArray(arr)
    print sol.segTree
    #print sol.sumRange(4, 4)
    #print sol.sumRange(2, 4)
    #print sol.sumRange(3, 3)
    sol.update(9, 27)
    #print sol.segTree
    #print sol.arr
    sol.update(1, -82)
    #print sol.segTree
    #print sol.arr
    sol.update(3, -72)
    #print sol.segTree
    #rint sol.arr
    print sol.sumRange(3, 7)
    #sol.update(1, 9)
    #print sol.sumRange(1, 8)
    #sol.update(3, 4)

    